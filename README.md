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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C120%20hrs%2029%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-430.70%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                976 commits         █████░░░░░░░░░░░░░░░░░░░░   20.64 % 
🌆 Daytime                1133 commits        ██████░░░░░░░░░░░░░░░░░░░   23.96 % 
🌃 Evening                1436 commits        ████████░░░░░░░░░░░░░░░░░   30.37 % 
🌙 Night                  1184 commits        ██████░░░░░░░░░░░░░░░░░░░   25.04 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   652 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.79 % 
Tuesday                  685 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.49 % 
Wednesday                514 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.87 % 
Thursday                 622 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.15 % 
Friday                   813 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.19 % 
Saturday                 501 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.59 % 
Sunday                   942 commits         █████░░░░░░░░░░░░░░░░░░░░   19.92 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Bash                     28 hrs 14 mins      ███████████████░░░░░░░░░░   60.21 % 
Ruby                     6 hrs 54 mins       ████░░░░░░░░░░░░░░░░░░░░░   14.74 % 
TypeScript               5 hrs 40 mins       ███░░░░░░░░░░░░░░░░░░░░░░   12.08 % 
Markdown                 2 hrs 58 mins       ██░░░░░░░░░░░░░░░░░░░░░░░   06.36 % 
JSONiq                   1 hr 15 mins        █░░░░░░░░░░░░░░░░░░░░░░░░   02.68 % 

💻 Operating System: 
WSL                      46 hrs 54 mins      █████████████████████████   100.00 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     9 repos             ████████████░░░░░░░░░░░░░   47.37 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.79 % 
JavaScript               3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.79 % 
TypeScript               2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   10.53 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
```




 Last Updated on 04/03/2026 18:46:36 UTC
<!--END_SECTION:waka-->
