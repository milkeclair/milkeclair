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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C080%20hrs%2019%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-442.17%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                1059 commits        ██████░░░░░░░░░░░░░░░░░░░   22.06 % 
🌆 Daytime                1109 commits        ██████░░░░░░░░░░░░░░░░░░░   23.10 % 
🌃 Evening                1443 commits        ████████░░░░░░░░░░░░░░░░░   30.06 % 
🌙 Night                  1190 commits        ██████░░░░░░░░░░░░░░░░░░░   24.79 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   696 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.50 % 
Tuesday                  692 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.41 % 
Wednesday                518 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.79 % 
Thursday                 635 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.23 % 
Friday                   820 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.08 % 
Saturday                 501 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.44 % 
Sunday                   939 commits         █████░░░░░░░░░░░░░░░░░░░░   19.56 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Bash                     19 hrs 15 mins      █████████████████░░░░░░░░   67.38 % 
Markdown                 3 hrs 37 mins       ███░░░░░░░░░░░░░░░░░░░░░░   12.67 % 
Ruby                     3 hrs 14 mins       ███░░░░░░░░░░░░░░░░░░░░░░   11.36 % 
TypeScript               1 hr 27 mins        █░░░░░░░░░░░░░░░░░░░░░░░░   05.09 % 
Other                    28 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   01.68 % 

💻 Operating System: 
WSL                      28 hrs 20 mins      █████████████████████████   99.13 % 
Mac                      14 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   00.87 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     10 repos            ████████████░░░░░░░░░░░░░   50.00 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.00 % 
JavaScript               3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.00 % 
TypeScript               2 repos             ██░░░░░░░░░░░░░░░░░░░░░░░   10.00 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.00 % 
```




 Last Updated on 26/02/2026 18:47:05 UTC
<!--END_SECTION:waka-->
