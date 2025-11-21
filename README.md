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
![Code Time](http://img.shields.io/badge/Code%20Time-1%2C655%20hrs%203%20mins-blue)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-316.4%20thousand%20lines%20of%20code-blue)

**I'm a Night 🦉** 

```text
🌞 Morning                748 commits         █████░░░░░░░░░░░░░░░░░░░░   21.01 % 
🌆 Daytime                812 commits         ██████░░░░░░░░░░░░░░░░░░░   22.81 % 
🌃 Evening                1026 commits        ███████░░░░░░░░░░░░░░░░░░   28.82 % 
🌙 Night                  974 commits         ███████░░░░░░░░░░░░░░░░░░   27.36 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   426 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.97 % 
Tuesday                  494 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.88 % 
Wednesday                425 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.94 % 
Thursday                 518 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.55 % 
Friday                   680 commits         █████░░░░░░░░░░░░░░░░░░░░   19.10 % 
Saturday                 319 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   08.96 % 
Sunday                   698 commits         █████░░░░░░░░░░░░░░░░░░░░   19.61 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Markdown                 10 hrs 7 mins       ███████░░░░░░░░░░░░░░░░░░   28.54 % 
Ruby                     9 hrs 54 mins       ███████░░░░░░░░░░░░░░░░░░   27.94 % 
JavaScript               5 hrs 27 mins       ████░░░░░░░░░░░░░░░░░░░░░   15.39 % 
TypeScript               4 hrs 39 mins       ███░░░░░░░░░░░░░░░░░░░░░░   13.15 % 
Bash                     4 hrs 35 mins       ███░░░░░░░░░░░░░░░░░░░░░░   12.96 % 

💻 Operating System: 
WSL                      22 hrs 25 mins      ████████████████░░░░░░░░░   63.22 % 
Mac                      13 hrs 3 mins       █████████░░░░░░░░░░░░░░░░   36.78 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     9 repos             ████████████░░░░░░░░░░░░░   50.00 % 
JavaScript               4 repos             ██████░░░░░░░░░░░░░░░░░░░   22.22 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   16.67 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.56 % 
Batchfile                1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.56 % 
```




 Last Updated on 21/11/2025 18:39:21 UTC
<!--END_SECTION:waka-->
