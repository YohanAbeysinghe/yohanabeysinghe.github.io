source "https://rubygems.org"

ruby "~> 3.3.0"
gem "jekyll", "~> 4.4"
gem "webrick", "~> 1.9"

# al-folio v1.2: keep runtime in the released gems. Optional demo features
# (analytics, comments, blogs, CV generation, search, notebooks) are not loaded.
group :jekyll_plugins do
  gem "jekyll-cache-bust"
  gem "jekyll-regex-replace"
  gem "jekyll-scholar", "~> 7.3"
  gem "jekyll-sitemap", "~> 1.4"
  gem "jekyll-socials"
  # Load the core after cache-bust so its gem-asset fallback is registered.
  gem "al_folio_core", "= 1.0.15"
  gem "al_folio_upgrade", "= 1.0.3"
end

gem "observer"
