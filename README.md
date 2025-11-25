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
![Code Time](http://img.shields.io/badge/Code%20Time-1%2C681%20hrs%2022%20mins-blue)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-325.2%20thousand%20lines%20of%20code-blue)

**I'm a Night 🦉** 

```text
🌞 Morning                767 commits         █████░░░░░░░░░░░░░░░░░░░░   20.09 % 
🌆 Daytime                897 commits         ██████░░░░░░░░░░░░░░░░░░░   23.49 % 
🌃 Evening                1131 commits        ███████░░░░░░░░░░░░░░░░░░   29.62 % 
🌙 Night                  1023 commits        ███████░░░░░░░░░░░░░░░░░░   26.79 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   491 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.86 % 
Tuesday                  551 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.43 % 
Wednesday                434 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.37 % 
Thursday                 539 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.12 % 
Friday                   691 commits         █████░░░░░░░░░░░░░░░░░░░░   18.10 % 
Saturday                 363 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   09.51 % 
Sunday                   749 commits         █████░░░░░░░░░░░░░░░░░░░░   19.62 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Ruby                     14 hrs 12 mins      ████████░░░░░░░░░░░░░░░░░   32.66 % 
Bash                     13 hrs 27 mins      ████████░░░░░░░░░░░░░░░░░   30.96 % 
Markdown                 9 hrs 10 mins       █████░░░░░░░░░░░░░░░░░░░░   21.09 % 
TypeScript               4 hrs 10 mins       ██░░░░░░░░░░░░░░░░░░░░░░░   09.60 % 
Other                    1 hr 54 mins        █░░░░░░░░░░░░░░░░░░░░░░░░   04.39 % 

💻 Operating System: 
WSL                      32 hrs 14 mins      ███████████████████░░░░░░   74.12 % 
Mac                      11 hrs 15 mins      ██████░░░░░░░░░░░░░░░░░░░   25.88 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     10 repos            █████████████░░░░░░░░░░░░   52.63 % 
JavaScript               4 repos             █████░░░░░░░░░░░░░░░░░░░░   21.05 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.79 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
Batchfile                1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
```




 Last Updated on 25/11/2025 18:43:36 UTC
<!--END_SECTION:waka-->
