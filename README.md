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
![Code Time](http://img.shields.io/badge/Code%20Time-1%2C671%20hrs%201%20min-blue)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-325.1%20thousand%20lines%20of%20code-blue)

**I'm a Night 🦉** 

```text
🌞 Morning                767 commits         █████░░░░░░░░░░░░░░░░░░░░   20.12 % 
🌆 Daytime                892 commits         ██████░░░░░░░░░░░░░░░░░░░   23.40 % 
🌃 Evening                1130 commits        ███████░░░░░░░░░░░░░░░░░░   29.64 % 
🌙 Night                  1023 commits        ███████░░░░░░░░░░░░░░░░░░   26.84 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   491 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.88 % 
Tuesday                  545 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.30 % 
Wednesday                434 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.39 % 
Thursday                 539 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.14 % 
Friday                   691 commits         █████░░░░░░░░░░░░░░░░░░░░   18.13 % 
Saturday                 363 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   09.52 % 
Sunday                   749 commits         █████░░░░░░░░░░░░░░░░░░░░   19.65 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Ruby                     13 hrs 20 mins      █████████░░░░░░░░░░░░░░░░   34.71 % 
Markdown                 11 hrs 13 mins      ███████░░░░░░░░░░░░░░░░░░   29.21 % 
Bash                     8 hrs 59 mins       ██████░░░░░░░░░░░░░░░░░░░   23.39 % 
TypeScript               2 hrs 33 mins       ██░░░░░░░░░░░░░░░░░░░░░░░   06.66 % 
Other                    1 hr 44 mins        █░░░░░░░░░░░░░░░░░░░░░░░░   04.52 % 

💻 Operating System: 
WSL                      27 hrs 12 mins      ██████████████████░░░░░░░   70.79 % 
Mac                      11 hrs 13 mins      ███████░░░░░░░░░░░░░░░░░░   29.21 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     10 repos            █████████████░░░░░░░░░░░░   52.63 % 
JavaScript               4 repos             █████░░░░░░░░░░░░░░░░░░░░   21.05 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.79 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
Batchfile                1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
```




 Last Updated on 24/11/2025 18:43:37 UTC
<!--END_SECTION:waka-->
