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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C350%20hrs%2059%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-486.00%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                1089 commits        █████░░░░░░░░░░░░░░░░░░░░   21.39 % 
🌆 Daytime                1192 commits        ██████░░░░░░░░░░░░░░░░░░░   23.41 % 
🌃 Evening                1547 commits        ████████░░░░░░░░░░░░░░░░░   30.39 % 
🌙 Night                  1263 commits        ██████░░░░░░░░░░░░░░░░░░░   24.81 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   708 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.91 % 
Tuesday                  727 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.28 % 
Wednesday                534 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.49 % 
Thursday                 658 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.92 % 
Friday                   872 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.13 % 
Saturday                 567 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.14 % 
Sunday                   1025 commits        █████░░░░░░░░░░░░░░░░░░░░   20.13 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Other                    8 hrs 11 mins       ██████████░░░░░░░░░░░░░░░   40.38 % 
Markdown                 6 hrs 43 mins       ████████░░░░░░░░░░░░░░░░░   33.13 % 
Bash                     1 hr 58 mins        ██░░░░░░░░░░░░░░░░░░░░░░░   09.75 % 
YAML                     1 hr 51 mins        ██░░░░░░░░░░░░░░░░░░░░░░░   09.17 % 
JSONiq                   31 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   02.55 % 

💻 Operating System: 
WSL                      10 hrs 24 mins      █████████████░░░░░░░░░░░░   51.31 % 
Mac                      9 hrs 52 mins       ████████████░░░░░░░░░░░░░   48.69 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     9 repos             ████████████░░░░░░░░░░░░░   47.37 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.79 % 
JavaScript               3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.79 % 
TypeScript               2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   10.53 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
```




 Last Updated on 05/05/2026 18:58:00 UTC
<!--END_SECTION:waka-->
