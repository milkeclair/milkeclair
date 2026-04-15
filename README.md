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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C304%20hrs%2019%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-485.55%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                1088 commits        █████░░░░░░░░░░░░░░░░░░░░   21.38 % 
🌆 Daytime                1192 commits        ██████░░░░░░░░░░░░░░░░░░░   23.43 % 
🌃 Evening                1547 commits        ████████░░░░░░░░░░░░░░░░░   30.40 % 
🌙 Night                  1261 commits        ██████░░░░░░░░░░░░░░░░░░░   24.78 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   708 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.92 % 
Tuesday                  726 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.27 % 
Wednesday                534 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.50 % 
Thursday                 658 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.93 % 
Friday                   870 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.10 % 
Saturday                 567 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.14 % 
Sunday                   1025 commits        █████░░░░░░░░░░░░░░░░░░░░   20.15 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Markdown                 13 hrs 28 mins      ███████████░░░░░░░░░░░░░░   44.15 % 
TypeScript               12 hrs 28 mins      ██████████░░░░░░░░░░░░░░░   40.85 % 
Ruby                     1 hr 29 mins        █░░░░░░░░░░░░░░░░░░░░░░░░   04.86 % 
Bash                     1 hr 8 mins         █░░░░░░░░░░░░░░░░░░░░░░░░   03.72 % 
Other                    50 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   02.75 % 

💻 Operating System: 
WSL                      30 hrs 25 mins      █████████████████████████   99.63 % 
Mac                      5 mins              ░░░░░░░░░░░░░░░░░░░░░░░░░   00.29 % 
Windows                  1 min               ░░░░░░░░░░░░░░░░░░░░░░░░░   00.07 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     9 repos             ████████████░░░░░░░░░░░░░   47.37 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.79 % 
JavaScript               3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.79 % 
TypeScript               2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   10.53 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
```




 Last Updated on 15/04/2026 18:52:00 UTC
<!--END_SECTION:waka-->
