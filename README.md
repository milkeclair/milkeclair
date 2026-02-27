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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C087%20hrs%2028%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-442.62%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                1059 commits        █████░░░░░░░░░░░░░░░░░░░░   21.96 % 
🌆 Daytime                1114 commits        ██████░░░░░░░░░░░░░░░░░░░   23.10 % 
🌃 Evening                1453 commits        ████████░░░░░░░░░░░░░░░░░   30.13 % 
🌙 Night                  1197 commits        ██████░░░░░░░░░░░░░░░░░░░   24.82 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   696 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.43 % 
Tuesday                  692 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.35 % 
Wednesday                518 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.74 % 
Thursday                 635 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.17 % 
Friday                   835 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.31 % 
Saturday                 508 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.53 % 
Sunday                   939 commits         █████░░░░░░░░░░░░░░░░░░░░   19.47 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Bash                     21 hrs 55 mins      ███████████████████░░░░░░   76.04 % 
TypeScript               2 hrs 25 mins       ██░░░░░░░░░░░░░░░░░░░░░░░   08.42 % 
Ruby                     1 hr 31 mins        █░░░░░░░░░░░░░░░░░░░░░░░░   05.29 % 
Markdown                 1 hr 31 mins        █░░░░░░░░░░░░░░░░░░░░░░░░   05.28 % 
Other                    36 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   02.08 % 

💻 Operating System: 
WSL                      28 hrs 35 mins      █████████████████████████   99.13 % 
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




 Last Updated on 27/02/2026 18:45:47 UTC
<!--END_SECTION:waka-->
