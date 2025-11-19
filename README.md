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
![Code Time](http://img.shields.io/badge/Code%20Time-1%2C645%20hrs%2013%20mins-blue)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-316.3%20thousand%20lines%20of%20code-blue)

**I'm a Night 🦉** 

```text
🌞 Morning                748 commits         █████░░░░░░░░░░░░░░░░░░░░   21.03 % 
🌆 Daytime                812 commits         ██████░░░░░░░░░░░░░░░░░░░   22.83 % 
🌃 Evening                1023 commits        ███████░░░░░░░░░░░░░░░░░░   28.76 % 
🌙 Night                  974 commits         ███████░░░░░░░░░░░░░░░░░░   27.38 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   426 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.98 % 
Tuesday                  494 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.89 % 
Wednesday                425 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.95 % 
Thursday                 515 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.48 % 
Friday                   680 commits         █████░░░░░░░░░░░░░░░░░░░░   19.12 % 
Saturday                 319 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   08.97 % 
Sunday                   698 commits         █████░░░░░░░░░░░░░░░░░░░░   19.62 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
JavaScript               10 hrs 51 mins      ███████░░░░░░░░░░░░░░░░░░   29.91 % 
Ruby                     10 hrs 22 mins      ███████░░░░░░░░░░░░░░░░░░   28.61 % 
TypeScript               5 hrs 26 mins       ████░░░░░░░░░░░░░░░░░░░░░   14.99 % 
Markdown                 5 hrs 22 mins       ████░░░░░░░░░░░░░░░░░░░░░   14.80 % 
Bash                     3 hrs 9 mins        ██░░░░░░░░░░░░░░░░░░░░░░░   08.69 % 

💻 Operating System: 
WSL                      27 hrs 33 mins      ███████████████████░░░░░░   75.91 % 
Mac                      8 hrs 44 mins       ██████░░░░░░░░░░░░░░░░░░░   24.09 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     9 repos             ████████████░░░░░░░░░░░░░   50.00 % 
JavaScript               4 repos             ██████░░░░░░░░░░░░░░░░░░░   22.22 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   16.67 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.56 % 
Batchfile                1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.56 % 
```




 Last Updated on 19/11/2025 18:42:53 UTC
<!--END_SECTION:waka-->
