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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C069%20hrs%2018%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-439.83%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                1059 commits        ██████░░░░░░░░░░░░░░░░░░░   22.22 % 
🌆 Daytime                1090 commits        ██████░░░░░░░░░░░░░░░░░░░   22.87 % 
🌃 Evening                1438 commits        ████████░░░░░░░░░░░░░░░░░   30.17 % 
🌙 Night                  1180 commits        ██████░░░░░░░░░░░░░░░░░░░   24.75 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   696 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.60 % 
Tuesday                  692 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.52 % 
Wednesday                513 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.76 % 
Thursday                 616 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.92 % 
Friday                   810 commits         ████░░░░░░░░░░░░░░░░░░░░░   16.99 % 
Saturday                 501 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.51 % 
Sunday                   939 commits         █████░░░░░░░░░░░░░░░░░░░░   19.70 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Bash                     10 hrs 31 mins      ████████████░░░░░░░░░░░░░   48.72 % 
Markdown                 4 hrs 43 mins       █████░░░░░░░░░░░░░░░░░░░░   21.87 % 
Ruby                     3 hrs 41 mins       ████░░░░░░░░░░░░░░░░░░░░░   17.12 % 
TypeScript               1 hr 15 mins        █░░░░░░░░░░░░░░░░░░░░░░░░   05.80 % 
Other                    32 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   02.50 % 

💻 Operating System: 
WSL                      21 hrs 12 mins      █████████████████████████   98.18 % 
Mac                      23 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   01.82 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     10 repos            ████████████░░░░░░░░░░░░░   50.00 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.00 % 
JavaScript               3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.00 % 
TypeScript               2 repos             ██░░░░░░░░░░░░░░░░░░░░░░░   10.00 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.00 % 
```




 Last Updated on 24/02/2026 18:47:58 UTC
<!--END_SECTION:waka-->
