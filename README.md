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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C507%20hrs%2015%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-603.41%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                1370 commits        █████░░░░░░░░░░░░░░░░░░░░   21.13 % 
🌆 Daytime                1554 commits        ██████░░░░░░░░░░░░░░░░░░░   23.97 % 
🌃 Evening                1883 commits        ███████░░░░░░░░░░░░░░░░░░   29.04 % 
🌙 Night                  1677 commits        ██████░░░░░░░░░░░░░░░░░░░   25.86 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   828 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.77 % 
Tuesday                  898 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.85 % 
Wednesday                641 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   09.89 % 
Thursday                 814 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.55 % 
Friday                   1198 commits        █████░░░░░░░░░░░░░░░░░░░░   18.48 % 
Saturday                 729 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.24 % 
Sunday                   1376 commits        █████░░░░░░░░░░░░░░░░░░░░   21.22 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Java                     11 hrs 33 mins      █████████░░░░░░░░░░░░░░░░   34.70 % 
Markdown                 8 hrs 8 mins        ██████░░░░░░░░░░░░░░░░░░░   24.44 % 
Kotlin                   4 hrs               ███░░░░░░░░░░░░░░░░░░░░░░   12.03 % 
Other                    2 hrs 16 mins       ██░░░░░░░░░░░░░░░░░░░░░░░   06.81 % 
Batchfile                1 hr 55 mins        █░░░░░░░░░░░░░░░░░░░░░░░░   05.78 % 

💻 Operating System: 
WSL                      26 hrs 1 min        ████████████████████░░░░░   78.13 % 
Mac                      6 hrs 33 mins       █████░░░░░░░░░░░░░░░░░░░░   19.68 % 
Windows                  43 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   02.18 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     9 repos             ████████████░░░░░░░░░░░░░   47.37 % 
TypeScript               2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   10.53 % 
Shell                    2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   10.53 % 
Java                     1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
```




 Last Updated on 03/06/2026 19:47:00 UTC
<!--END_SECTION:waka-->
