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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C475%20hrs%2028%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-609.35%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                1373 commits        █████░░░░░░░░░░░░░░░░░░░░   21.12 % 
🌆 Daytime                1558 commits        ██████░░░░░░░░░░░░░░░░░░░   23.96 % 
🌃 Evening                1894 commits        ███████░░░░░░░░░░░░░░░░░░   29.13 % 
🌙 Night                  1677 commits        ██████░░░░░░░░░░░░░░░░░░░   25.79 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   830 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.77 % 
Tuesday                  898 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.81 % 
Wednesday                651 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.01 % 
Thursday                 812 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.49 % 
Friday                   1202 commits        █████░░░░░░░░░░░░░░░░░░░░   18.49 % 
Saturday                 733 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.27 % 
Sunday                   1376 commits        █████░░░░░░░░░░░░░░░░░░░░   21.16 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Markdown                 11 hrs 16 mins      ██████████░░░░░░░░░░░░░░░   40.62 % 
Ruby                     4 hrs 57 mins       ████░░░░░░░░░░░░░░░░░░░░░   17.89 % 
Other                    2 hrs 55 mins       ███░░░░░░░░░░░░░░░░░░░░░░   10.54 % 
TypeScript               2 hrs 34 mins       ██░░░░░░░░░░░░░░░░░░░░░░░   09.27 % 
PowerShell               1 hr 53 mins        ██░░░░░░░░░░░░░░░░░░░░░░░   06.83 % 

💻 Operating System: 
Mac                      12 hrs 16 mins      ███████████░░░░░░░░░░░░░░   44.22 % 
WSL                      9 hrs 34 mins       █████████░░░░░░░░░░░░░░░░   34.52 % 
Windows                  5 hrs 54 mins       █████░░░░░░░░░░░░░░░░░░░░   21.26 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     9 repos             ████████████░░░░░░░░░░░░░   47.37 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.79 % 
JavaScript               3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.79 % 
TypeScript               2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   10.53 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
```




 Last Updated on 29/05/2026 19:21:15 UTC
<!--END_SECTION:waka-->
