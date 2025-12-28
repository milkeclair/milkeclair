```ruby
Milkeclair.profile do |me|
 me.description do
  intro "ひよっこ"
  enjoy "自分が欲しいものを作ります"
  good  "ほんのちょっとだけRubyができる"
 end

 me.stack do
  languages  :ruby, :shell_script
  frameworks :ruby_on_rails
 end

 me.interests :dsl, :vanilla_coding, :domain_modeling
end
```

<details>
<summary>definitions</summary>

```ruby
class Milkeclair
 include Singleton

 attr_accessor :descriptions, :fav_languages, :fav_frameworks, :interests

 def initialize
  @descriptions   = []
  @fav_languages  = []
  @fav_frameworks = []
  @interests      = []
 end

 def self.profile(&block) = block.call(instance)

 def description(&block) = instance_eval(&block)
 alias_method :stack, :description

 def intro(text) = self.descriptions << text
 alias_method :enjoy, :intro
 alias_method :good,  :intro

 def languages(*)  = self.fav_languages  = [*]
 def frameworks(*) = self.fav_frameworks = [*]
 def interests(*)  = self.interests      = [*]
end
```
</details>

[![stats](https://github-readme-stats.vercel.app/api/wakatime?username=milkeclair&layout=compact&disable_animations=true&langs_count=20&card_width=1010&bg_color=262c36&hide_border=true&text_color=d1d7e0&title_color=d1d7e0)](https://github.com/anuraghazra/github-readme-stats)

<!--START_SECTION:waka-->
![Code Time](http://img.shields.io/badge/Code%20Time-1%2C878%20hrs%2044%20mins-blue)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-386.2%20thousand%20lines%20of%20code-blue)

**I'm a Night 🦉** 

```text
🌞 Morning                922 commits         █████░░░░░░░░░░░░░░░░░░░░   21.76 % 
🌆 Daytime                963 commits         ██████░░░░░░░░░░░░░░░░░░░   22.72 % 
🌃 Evening                1274 commits        ████████░░░░░░░░░░░░░░░░░   30.06 % 
🌙 Night                  1079 commits        ██████░░░░░░░░░░░░░░░░░░░   25.46 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   570 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.45 % 
Tuesday                  597 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.09 % 
Wednesday                478 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.28 % 
Thursday                 566 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.36 % 
Friday                   756 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.84 % 
Saturday                 422 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   09.96 % 
Sunday                   849 commits         █████░░░░░░░░░░░░░░░░░░░░   20.03 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Ruby                     24 hrs 58 mins      ███████████████████████░░   90.11 % 
Markdown                 46 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   02.77 % 
JavaScript               44 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   02.69 % 
TypeScript               36 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   02.22 % 
ERB                      33 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   02.03 % 

💻 Operating System: 
WSL                      27 hrs 14 mins      █████████████████████████   98.29 % 
Mac                      28 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   01.71 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     10 repos            ████████████░░░░░░░░░░░░░   47.62 % 
JavaScript               4 repos             █████░░░░░░░░░░░░░░░░░░░░   19.05 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   14.29 % 
TypeScript               2 repos             ██░░░░░░░░░░░░░░░░░░░░░░░   09.52 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   04.76 % 
```




 Last Updated on 28/12/2025 18:42:42 UTC
<!--END_SECTION:waka-->
