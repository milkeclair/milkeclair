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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C451%20hrs%2034%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-540.93%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                1193 commits        █████░░░░░░░░░░░░░░░░░░░░   21.89 % 
🌆 Daytime                1265 commits        ██████░░░░░░░░░░░░░░░░░░░   23.22 % 
🌃 Evening                1654 commits        ████████░░░░░░░░░░░░░░░░░   30.35 % 
🌙 Night                  1337 commits        ██████░░░░░░░░░░░░░░░░░░░   24.54 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   770 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.13 % 
Tuesday                  768 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.09 % 
Wednesday                549 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.08 % 
Thursday                 692 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.70 % 
Friday                   931 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.09 % 
Saturday                 623 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.43 % 
Sunday                   1116 commits        █████░░░░░░░░░░░░░░░░░░░░   20.48 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Ruby                     8 hrs 23 mins       █████████████░░░░░░░░░░░░   51.98 % 
TypeScript               3 hrs 12 mins       █████░░░░░░░░░░░░░░░░░░░░   19.85 % 
Markdown                 1 hr 53 mins        ███░░░░░░░░░░░░░░░░░░░░░░   11.67 % 
Python                   1 hr 18 mins        ██░░░░░░░░░░░░░░░░░░░░░░░   08.12 % 
Bash                     55 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   05.76 % 

💻 Operating System: 
WSL                      15 hrs 56 mins      █████████████████████████   99.98 % 
Mac                      0 secs              ░░░░░░░░░░░░░░░░░░░░░░░░░   00.02 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     9 repos             ████████████░░░░░░░░░░░░░   47.37 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.79 % 
JavaScript               3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.79 % 
TypeScript               2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   10.53 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
```




 Last Updated on 24/05/2026 18:51:28 UTC
<!--END_SECTION:waka-->
