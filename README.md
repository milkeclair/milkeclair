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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C589%20hrs%2054%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-575.54%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                1285 commits        █████░░░░░░░░░░░░░░░░░░░░   20.64 % 
🌆 Daytime                1510 commits        ██████░░░░░░░░░░░░░░░░░░░   24.25 % 
🌃 Evening                1787 commits        ███████░░░░░░░░░░░░░░░░░░   28.70 % 
🌙 Night                  1645 commits        ███████░░░░░░░░░░░░░░░░░░   26.42 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   775 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.45 % 
Tuesday                  858 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.78 % 
Wednesday                627 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.07 % 
Thursday                 803 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.90 % 
Friday                   1180 commits        █████░░░░░░░░░░░░░░░░░░░░   18.95 % 
Saturday                 687 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.03 % 
Sunday                   1297 commits        █████░░░░░░░░░░░░░░░░░░░░   20.83 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Bash                     16 hrs 49 mins      ██████████████████░░░░░░░   72.01 % 
Markdown                 2 hrs 37 mins       ███░░░░░░░░░░░░░░░░░░░░░░   11.25 % 
Ruby                     57 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   04.09 % 
TypeScript               50 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   03.60 % 
Other                    43 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   03.12 % 

💻 Operating System: 
WSL                      23 hrs 11 mins      █████████████████████████   99.20 % 
Mac                      11 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   00.80 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     9 repos             ████████████░░░░░░░░░░░░░   47.37 % 
TypeScript               2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   10.53 % 
Shell                    2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   10.53 % 
Java                     1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
```




 Last Updated on 23/06/2026 19:14:33 UTC
<!--END_SECTION:waka-->
