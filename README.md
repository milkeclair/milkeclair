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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C603%20hrs%2051%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-595.26%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                1387 commits        █████░░░░░░░░░░░░░░░░░░░░   21.56 % 
🌆 Daytime                1524 commits        ██████░░░░░░░░░░░░░░░░░░░   23.69 % 
🌃 Evening                1808 commits        ███████░░░░░░░░░░░░░░░░░░   28.10 % 
🌙 Night                  1715 commits        ███████░░░░░░░░░░░░░░░░░░   26.66 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   794 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.34 % 
Tuesday                  882 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.71 % 
Wednesday                615 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   09.56 % 
Thursday                 811 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.60 % 
Friday                   1244 commits        █████░░░░░░░░░░░░░░░░░░░░   19.33 % 
Saturday                 718 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.16 % 
Sunday                   1370 commits        █████░░░░░░░░░░░░░░░░░░░░   21.29 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Markdown                 6 hrs 39 mins       ██████████░░░░░░░░░░░░░░░   41.66 % 
Ruby                     4 hrs               ██████░░░░░░░░░░░░░░░░░░░   25.05 % 
Bash                     3 hrs 47 mins       ██████░░░░░░░░░░░░░░░░░░░   23.77 % 
TypeScript               52 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   05.52 % 
Python                   15 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   01.65 % 

💻 Operating System: 
WSL                      14 hrs 20 mins      ██████████████████████░░░   89.70 % 
Mac                      1 hr 33 mins        ██░░░░░░░░░░░░░░░░░░░░░░░   09.76 % 
Windows                  5 mins              ░░░░░░░░░░░░░░░░░░░░░░░░░   00.54 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     8 repos             █████████████░░░░░░░░░░░░   53.33 % 
TypeScript               2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   13.33 % 
Java                     1 repo              ██░░░░░░░░░░░░░░░░░░░░░░░   06.67 % 
Shell                    1 repo              ██░░░░░░░░░░░░░░░░░░░░░░░   06.67 % 
CSS                      1 repo              ██░░░░░░░░░░░░░░░░░░░░░░░   06.67 % 
```




 Last Updated on 28/06/2026 18:53:29 UTC
<!--END_SECTION:waka-->
