require "active_support/all"
require 'net/http'
require 'json'
require 'uri'

module Jekyll
  # Renders a single number from the INSPIRE-HEP author citation summary,
  # i.e. the same aggregation shown on https://inspirehep.net/authors/<id>
  #
  #   {% inspirehep_author_summary citations %}
  #   {% inspirehep_author_summary h_index exclude_self %}
  #
  # Available metrics: papers, citations, h_index, average_citations
  # (each also as *_published, restricted to published papers).
  class InspireHEPAuthorSummaryTag < Liquid::Tag
    Summaries = {}
    Bais = {}

    def initialize(tag_name, params, tokens)
      super
      args = params.strip.split(/\s+/)
      @metric = args.shift.to_s
      @exclude_self = args.include?("exclude_self")
    end

    def render(context)
      author_id = context.registers[:site].config["inspirehep_id"]
      return "N/A" if author_id.nil?

      summary = summary_for(author_id, @exclude_self)
      value = summary && summary[@metric]
      return "N/A" if value.nil?

      if @metric.start_with?("average")
        format("%.1f", value)
      else
        Helpers.number_to_delimited(value.to_i)
      end
    end

    private

    module Helpers
      extend ActiveSupport::NumberHelper
    end

    def get_json(url)
      JSON.parse(Net::HTTP.get(URI(url)))
    end

    # The citation-summary facet is only queryable by BAI, so resolve it from
    # the numeric author id configured in _config.yml.
    def bai_for(author_id)
      return Bais[author_id] if Bais.key?(author_id)

      data = get_json("https://inspirehep.net/api/authors/#{author_id}?fields=ids")
      ids = data.dig("metadata", "ids") || []
      Bais[author_id] = ids.find { |id| id["schema"] == "INSPIRE BAI" }&.fetch("value")
    end

    def summary_for(author_id, exclude_self)
      key = [author_id, exclude_self]
      return Summaries[key] if Summaries.key?(key)

      Summaries[key] = begin
        bai = bai_for(author_id)
        raise "no INSPIRE BAI for author #{author_id}" if bai.nil?

        url = "https://inspirehep.net/api/literature/facets?q=a%20#{bai}&facet_name=citation-summary"
        url += "&exclude-self-citations=true" if exclude_self
        agg = get_json(url).dig("aggregations", "citation_summary")
        raise "empty citation summary for #{bai}" if agg.nil?

        buckets = agg.dig("citations", "buckets")
        {
          "papers" => buckets.dig("all", "doc_count"),
          "papers_published" => buckets.dig("published", "doc_count"),
          "citations" => buckets.dig("all", "citations_count", "value"),
          "citations_published" => buckets.dig("published", "citations_count", "value"),
          "average_citations" => buckets.dig("all", "average_citations", "value"),
          "average_citations_published" => buckets.dig("published", "average_citations", "value"),
          "h_index" => agg.dig("h-index", "value", "all"),
          "h_index_published" => agg.dig("h-index", "value", "published"),
        }
      rescue Exception => e
        puts "Error fetching INSPIRE citation summary for #{author_id}: #{e.class} - #{e.message}"
        nil
      end
    end
  end
end

Liquid::Template.register_tag('inspirehep_author_summary', Jekyll::InspireHEPAuthorSummaryTag)
