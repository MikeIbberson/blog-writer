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

export default {
  layout: "essay.njk",
  permalink: (data) => `/essays/${data.page.fileSlug}/`,
  eleventyComputed: {
    title: (data) => titleFromMarkdown(data.page.rawInput),
    description: (data) => excerptFromMarkdown(data.page.rawInput),
  },
};
