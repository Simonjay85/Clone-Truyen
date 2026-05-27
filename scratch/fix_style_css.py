with open('tehi-theme/assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Fix vh-news-detail-tags-item
old_tags_block = """  border-radius: 50px;
  color: #000000;
  font-size: 0.8rem;
  font-family: Inter-light;
  -webkit-transition: all 0.3s ease-in-out;
  -moz-transition: all 0.3s ease-in-out;
  -ms-transition: all 0.3s ease-in-out;
  -o-transition: all 0.3s ease-in-out;
  transition: all 0.3s ease-in-out;
  -webkit-border-radius: 50px;
  -moz-border-radius: 50px;
  -ms-border-radius: 50px;
  -o-border-radius: 50px;"""
new_tags_block = """  color: #000000;
  font-size: 0.8rem;
  font-family: Inter-light;
  -webkit-transition: all 0.3s ease-in-out;
  -moz-transition: all 0.3s ease-in-out;
  -ms-transition: all 0.3s ease-in-out;
  -o-transition: all 0.3s ease-in-out;
  transition: all 0.3s ease-in-out;
  -webkit-border-radius: 50px;
  -moz-border-radius: 50px;
  -ms-border-radius: 50px;
  -o-border-radius: 50px;
  border-radius: 50px;"""
css = css.replace(old_tags_block, new_tags_block)

# 2. Fix vh-news-detail-btn-search
old_btn_search = """  border-radius: 0;
  -webkit-border-radius: 0;
  -moz-border-radius: 0;
  -ms-border-radius: 0;
  -o-border-radius: 0;"""
new_btn_search = """  -webkit-border-radius: 0;
  -moz-border-radius: 0;
  -ms-border-radius: 0;
  -o-border-radius: 0;
  border-radius: 0;"""
# Using general replace for border-radius: 0; with prefixes (will handle both btn-search and form-control!)
css = css.replace(old_btn_search, new_btn_search)

with open('tehi-theme/assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Style CSS tags and search button borders fixed successfully!")
