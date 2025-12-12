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
![Code Time](http://img.shields.io/badge/Code%20Time-1%2C799%20hrs%2011%20mins-blue)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-343.6%20thousand%20lines%20of%20code-blue)

**I'm a Night 🦉** 

```text
🌞 Morning                803 commits         █████░░░░░░░░░░░░░░░░░░░░   20.48 % 
🌆 Daytime                903 commits         ██████░░░░░░░░░░░░░░░░░░░   23.03 % 
🌃 Evening                1178 commits        ████████░░░░░░░░░░░░░░░░░   30.04 % 
🌙 Night                  1037 commits        ███████░░░░░░░░░░░░░░░░░░   26.45 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   509 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.98 % 
Tuesday                  556 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.18 % 
Wednesday                450 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.48 % 
Thursday                 540 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.77 % 
Friday                   707 commits         █████░░░░░░░░░░░░░░░░░░░░   18.03 % 
Saturday                 385 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   09.82 % 
Sunday                   774 commits         █████░░░░░░░░░░░░░░░░░░░░   19.74 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
TypeScript               27 hrs 57 mins      ██████████████████░░░░░░░   70.85 % 
Ruby                     7 hrs 53 mins       █████░░░░░░░░░░░░░░░░░░░░   20.01 % 
Markdown                 2 hrs 13 mins       █░░░░░░░░░░░░░░░░░░░░░░░░   05.62 % 
JSON                     37 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   01.59 % 
EJS                      21 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   00.91 % 

💻 Operating System: 
WSL                      33 hrs 7 mins       █████████████████████░░░░   83.93 % 
Mac                      6 hrs 20 mins       ████░░░░░░░░░░░░░░░░░░░░░   16.07 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     10 repos            ████████████░░░░░░░░░░░░░   47.62 % 
JavaScript               4 repos             █████░░░░░░░░░░░░░░░░░░░░   19.05 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   14.29 % 
TypeScript               2 repos             ██░░░░░░░░░░░░░░░░░░░░░░░   09.52 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   04.76 % 
```




 Last Updated on 12/12/2025 18:44:41 UTC
<!--END_SECTION:waka-->
