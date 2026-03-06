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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C138%20hrs%2027%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-430.96%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                976 commits         █████░░░░░░░░░░░░░░░░░░░░   20.62 % 
🌆 Daytime                1133 commits        ██████░░░░░░░░░░░░░░░░░░░   23.93 % 
🌃 Evening                1437 commits        ████████░░░░░░░░░░░░░░░░░   30.35 % 
🌙 Night                  1188 commits        ██████░░░░░░░░░░░░░░░░░░░   25.10 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   652 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.77 % 
Tuesday                  685 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.47 % 
Wednesday                514 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.86 % 
Thursday                 623 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.16 % 
Friday                   813 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.17 % 
Saturday                 505 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.67 % 
Sunday                   942 commits         █████░░░░░░░░░░░░░░░░░░░░   19.90 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Bash                     24 hrs 48 mins      █████████████░░░░░░░░░░░░   50.12 % 
Markdown                 8 hrs 1 min         ████░░░░░░░░░░░░░░░░░░░░░   16.22 % 
Ruby                     7 hrs 12 mins       ████░░░░░░░░░░░░░░░░░░░░░   14.55 % 
TypeScript               4 hrs 24 mins       ██░░░░░░░░░░░░░░░░░░░░░░░   08.92 % 
JSONiq                   3 hrs 21 mins       ██░░░░░░░░░░░░░░░░░░░░░░░   06.80 % 

💻 Operating System: 
WSL                      49 hrs 29 mins      █████████████████████████   100.00 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     9 repos             ████████████░░░░░░░░░░░░░   47.37 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.79 % 
JavaScript               3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.79 % 
TypeScript               2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   10.53 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
```




 Last Updated on 06/03/2026 18:46:29 UTC
<!--END_SECTION:waka-->
