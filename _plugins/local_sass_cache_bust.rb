# Include local Sass overrides in the theme's stylesheet cache key.
# The core theme currently hashes its gem partials but omits this site's _sass/.
require "digest"

module LocalSassCacheBust
  def bust_css_cache(file_name)
    theme_versioned_path = super
    source = @context.registers[:site].source
    local_files = Dir[File.join(source, "_sass", "**", "*.scss")].sort
    local_files += Dir[File.join(source, "assets", "css", "*.scss")].sort
    local_digest = Digest::SHA256.hexdigest(local_files.map { |path| File.binread(path) }.join)[0, 16]
    "#{theme_versioned_path}-#{local_digest}"
  end
end

Jekyll::CacheBust.prepend(LocalSassCacheBust)
