/** Rewrite catalogue-relative URLs so they resolve under the Pages base path. */
function rewriteCatalogueUrls(content, pathPrefix) {
  if (!content) return content;

  const prefix = pathPrefix.replace(/\/$/, "");

  return content
    .replace(/(src|href)="\.\/assets\//g, `$1="${prefix}/assets/`)
    .replace(
      /href="\.\/(\d{2}-[a-z0-9-]+)\.md"/g,
      `href="${prefix}/essays/$1/"`
    );
}

function titleFromMarkdown(raw) {
  const match = String(raw || "").match(/^#\s+(.+)$/m);
  return match ? match[1].trim() : "Untitled";
}

function excerptFromMarkdown(raw) {
  const withoutHeading = String(raw || "").replace(/^#\s+.+$/m, "");
  const withoutImages = withoutHeading.replace(/!\[[^\]]*\]\([^)]+\)/g, "");
  const plain = withoutImages
    .replace(/\[([^\]]+)\]\([^)]+\)/g, "$1")
    .replace(/[*_`]/g, "");
  const paragraphs = plain
    .split(/\n\s*\n/)
    .map((p) => p.replace(/\s+/g, " ").trim())
    .filter(
      (p) =>
        p.length > 0 &&
        !p.startsWith("---") &&
        !p.startsWith("|") &&
        !p.startsWith("#")
    );
  const first = paragraphs[0] || "";
  return first.length > 220 ? `${first.slice(0, 217).trim()}…` : first;
}

export default function (eleventyConfig) {
  const pathPrefix = "/blog-writer/";

  eleventyConfig.addPassthroughCopy({ "catalogue/assets": "assets" });
  eleventyConfig.addPassthroughCopy({ "src/css": "css" });

  eleventyConfig.addCollection("essays", (collectionApi) => {
    return collectionApi
      .getFilteredByGlob("catalogue/*.md")
      .sort((a, b) => a.inputPath.localeCompare(b.inputPath));
  });

  eleventyConfig.addTransform("rewriteCatalogueUrls", (content, outputPath) => {
    if (outputPath && outputPath.endsWith(".html")) {
      return rewriteCatalogueUrls(content, pathPrefix);
    }
    return content;
  });

  eleventyConfig.addFilter("mdTitle", (raw) => titleFromMarkdown(raw));
  eleventyConfig.addFilter("mdExcerpt", (raw) => excerptFromMarkdown(raw));

  eleventyConfig.addFilter("essayNumber", (fileSlug) => {
    const match = String(fileSlug).match(/^(\d{2})-/);
    return match ? match[1] : "";
  });

  eleventyConfig.addFilter("siblingEssay", (collection, page, direction) => {
    const index = collection.findIndex((item) => item.url === page.url);
    if (index === -1) return null;
    if (direction === "prev") {
      return index > 0 ? collection[index - 1] : null;
    }
    if (direction === "next") {
      return index < collection.length - 1 ? collection[index + 1] : null;
    }
    return null;
  });

  eleventyConfig.ignores.add("samples/**");
  eleventyConfig.ignores.add("AGENTS.md");
  eleventyConfig.ignores.add("README.md");
  eleventyConfig.ignores.add(".cursor/**");
  eleventyConfig.ignores.add("package.json");
  eleventyConfig.ignores.add("package-lock.json");

  return {
    pathPrefix,
    dir: {
      input: ".",
      includes: "src/_includes",
      layouts: "src/_includes",
      output: "_site",
    },
    markdownTemplateEngine: false,
    htmlTemplateEngine: "njk",
    templateFormats: ["md", "njk", "html"],
  };
}
