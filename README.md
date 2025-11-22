```ruby
Milkeclair.profile do |me|
 me.description do
  intro "ひよっこ開発者"
  enjoy "自分が欲しいものを作ります"
  good  "バックエンドがほんのちょっとだけできます"
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
![Code Time](http://img.shields.io/badge/Code%20Time-1%2C655%20hrs%2027%20mins-blue)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-316.5%20thousand%20lines%20of%20code-blue)

**I'm a Night 🦉** 

```text
🌞 Morning                748 commits         █████░░░░░░░░░░░░░░░░░░░░   20.99 % 
🌆 Daytime                812 commits         ██████░░░░░░░░░░░░░░░░░░░   22.79 % 
🌃 Evening                1029 commits        ███████░░░░░░░░░░░░░░░░░░   28.88 % 
🌙 Night                  974 commits         ███████░░░░░░░░░░░░░░░░░░   27.34 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   426 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.96 % 
Tuesday                  494 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.86 % 
Wednesday                425 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.93 % 
Thursday                 518 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.54 % 
Friday                   680 commits         █████░░░░░░░░░░░░░░░░░░░░   19.09 % 
Saturday                 322 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   09.04 % 
Sunday                   698 commits         █████░░░░░░░░░░░░░░░░░░░░   19.59 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Markdown                 10 hrs 34 mins      █████████░░░░░░░░░░░░░░░░   34.10 % 
Ruby                     10 hrs 29 mins      ████████░░░░░░░░░░░░░░░░░   33.84 % 
Bash                     4 hrs 45 mins       ████░░░░░░░░░░░░░░░░░░░░░   15.35 % 
TypeScript               4 hrs 29 mins       ████░░░░░░░░░░░░░░░░░░░░░   14.47 % 
JSON                     17 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   00.95 % 

💻 Operating System: 
WSL                      19 hrs 33 mins      ████████████████░░░░░░░░░   63.06 % 
Mac                      11 hrs 27 mins      █████████░░░░░░░░░░░░░░░░   36.94 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     9 repos             ████████████░░░░░░░░░░░░░   50.00 % 
JavaScript               4 repos             ██████░░░░░░░░░░░░░░░░░░░   22.22 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   16.67 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.56 % 
Batchfile                1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.56 % 
```




 Last Updated on 22/11/2025 18:39:38 UTC
<!--END_SECTION:waka-->
