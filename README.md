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
![Code Time](http://img.shields.io/badge/Code%20Time-1%2C873%20hrs%2020%20mins-blue)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-385.3%20thousand%20lines%20of%20code-blue)

**I'm a Night 🦉** 

```text
🌞 Morning                922 commits         █████░░░░░░░░░░░░░░░░░░░░   21.78 % 
🌆 Daytime                963 commits         ██████░░░░░░░░░░░░░░░░░░░   22.74 % 
🌃 Evening                1272 commits        ████████░░░░░░░░░░░░░░░░░   30.04 % 
🌙 Night                  1077 commits        ██████░░░░░░░░░░░░░░░░░░░   25.44 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   570 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.46 % 
Tuesday                  597 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.10 % 
Wednesday                478 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.29 % 
Thursday                 566 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.37 % 
Friday                   756 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.86 % 
Saturday                 420 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   09.92 % 
Sunday                   847 commits         █████░░░░░░░░░░░░░░░░░░░░   20.00 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Ruby                     37 hrs 39 mins      ██████████████████████░░░   86.18 % 
ERB                      1 hr 40 mins        █░░░░░░░░░░░░░░░░░░░░░░░░   03.85 % 
TypeScript               1 hr 38 mins        █░░░░░░░░░░░░░░░░░░░░░░░░   03.77 % 
JavaScript               1 hr 3 mins         █░░░░░░░░░░░░░░░░░░░░░░░░   02.40 % 
Markdown                 48 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   01.85 % 

💻 Operating System: 
WSL                      41 hrs 20 mins      ████████████████████████░   94.58 % 
Mac                      2 hrs 22 mins       █░░░░░░░░░░░░░░░░░░░░░░░░   05.42 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     10 repos            ████████████░░░░░░░░░░░░░   47.62 % 
JavaScript               4 repos             █████░░░░░░░░░░░░░░░░░░░░   19.05 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   14.29 % 
TypeScript               2 repos             ██░░░░░░░░░░░░░░░░░░░░░░░   09.52 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   04.76 % 
```




 Last Updated on 24/12/2025 18:43:01 UTC
<!--END_SECTION:waka-->
