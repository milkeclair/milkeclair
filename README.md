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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C407%20hrs%206%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-540.42%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                1193 commits        █████░░░░░░░░░░░░░░░░░░░░   21.91 % 
🌆 Daytime                1265 commits        ██████░░░░░░░░░░░░░░░░░░░   23.23 % 
🌃 Evening                1654 commits        ████████░░░░░░░░░░░░░░░░░   30.38 % 
🌙 Night                  1333 commits        ██████░░░░░░░░░░░░░░░░░░░   24.48 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   770 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.14 % 
Tuesday                  768 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.10 % 
Wednesday                548 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.06 % 
Thursday                 692 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.71 % 
Friday                   928 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.04 % 
Saturday                 623 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.44 % 
Sunday                   1116 commits        █████░░░░░░░░░░░░░░░░░░░░   20.50 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Other                    22 hrs 17 mins      ██████████░░░░░░░░░░░░░░░   39.71 % 
Ruby                     12 hrs 52 mins      ██████░░░░░░░░░░░░░░░░░░░   22.94 % 
Markdown                 6 hrs 27 mins       ███░░░░░░░░░░░░░░░░░░░░░░   11.51 % 
Bash                     6 hrs 20 mins       ███░░░░░░░░░░░░░░░░░░░░░░   11.31 % 
JSON                     2 hrs 42 mins       █░░░░░░░░░░░░░░░░░░░░░░░░   04.84 % 

💻 Operating System: 
WSL                      55 hrs 34 mins      █████████████████████████   99.03 % 
Windows                  32 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   00.97 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     9 repos             ████████████░░░░░░░░░░░░░   47.37 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.79 % 
JavaScript               3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.79 % 
TypeScript               2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   10.53 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
```




 Last Updated on 13/05/2026 19:08:17 UTC
<!--END_SECTION:waka-->
