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

 def languages(*)  = self.fav_languages = [*]
 def frameworks(*) = self.fav_frameworks = [*]
 def interests(*)  = self.interests = [*]
end
```
</details>

[![stats](https://github-readme-stats.vercel.app/api/wakatime?username=milkeclair&layout=compact&disable_animations=true&langs_count=20&card_width=1010&bg_color=262c36&hide_border=true&text_color=d1d7e0&title_color=d1d7e0)](https://github.com/anuraghazra/github-readme-stats)

<!--START_SECTION:waka-->
![Code Time](http://img.shields.io/badge/Code%20Time-1%2C624%20hrs%2027%20mins-blue)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-318.5%20thousand%20lines%20of%20code-blue)

**I'm a Night 🦉** 

```text
🌞 Morning                762 commits         █████░░░░░░░░░░░░░░░░░░░░   21.07 % 
🌆 Daytime                818 commits         ██████░░░░░░░░░░░░░░░░░░░   22.62 % 
🌃 Evening                1035 commits        ███████░░░░░░░░░░░░░░░░░░   28.61 % 
🌙 Night                  1002 commits        ███████░░░░░░░░░░░░░░░░░░   27.70 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   442 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.22 % 
Tuesday                  504 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.93 % 
Wednesday                424 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.72 % 
Thursday                 515 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.24 % 
Friday                   684 commits         █████░░░░░░░░░░░░░░░░░░░░   18.91 % 
Saturday                 338 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   09.34 % 
Sunday                   710 commits         █████░░░░░░░░░░░░░░░░░░░░   19.63 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Ruby                     19 hrs 2 mins       █████████░░░░░░░░░░░░░░░░   34.55 % 
JavaScript               10 hrs 46 mins      █████░░░░░░░░░░░░░░░░░░░░   19.55 % 
TypeScript               10 hrs 11 mins      █████░░░░░░░░░░░░░░░░░░░░   18.49 % 
Markdown                 7 hrs 37 mins       ███░░░░░░░░░░░░░░░░░░░░░░   13.83 % 
Bash                     2 hrs 57 mins       █░░░░░░░░░░░░░░░░░░░░░░░░   05.37 % 

💻 Operating System: 
WSL                      46 hrs 39 mins      █████████████████████░░░░   84.63 % 
Mac                      8 hrs 28 mins       ████░░░░░░░░░░░░░░░░░░░░░   15.37 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     9 repos             ████████████░░░░░░░░░░░░░   50.00 % 
JavaScript               4 repos             ██████░░░░░░░░░░░░░░░░░░░   22.22 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   16.67 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.56 % 
Batchfile                1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.56 % 
```




 Last Updated on 15/11/2025 18:39:50 UTC
<!--END_SECTION:waka-->
