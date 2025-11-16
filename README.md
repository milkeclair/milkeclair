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
![Code Time](http://img.shields.io/badge/Code%20Time-1%2C626%20hrs%2046%20mins-blue)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-318.5%20thousand%20lines%20of%20code-blue)

**I'm a Night 🦉** 

```text
🌞 Morning                762 commits         █████░░░░░░░░░░░░░░░░░░░░   21.05 % 
🌆 Daytime                819 commits         ██████░░░░░░░░░░░░░░░░░░░   22.62 % 
🌃 Evening                1036 commits        ███████░░░░░░░░░░░░░░░░░░   28.62 % 
🌙 Night                  1003 commits        ███████░░░░░░░░░░░░░░░░░░   27.71 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   442 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.21 % 
Tuesday                  504 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.92 % 
Wednesday                424 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.71 % 
Thursday                 515 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.23 % 
Friday                   684 commits         █████░░░░░░░░░░░░░░░░░░░░   18.90 % 
Saturday                 338 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   09.34 % 
Sunday                   713 commits         █████░░░░░░░░░░░░░░░░░░░░   19.70 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Ruby                     13 hrs 36 mins      ███████░░░░░░░░░░░░░░░░░░   26.63 % 
TypeScript               11 hrs 52 mins      ██████░░░░░░░░░░░░░░░░░░░   23.25 % 
JavaScript               10 hrs 51 mins      █████░░░░░░░░░░░░░░░░░░░░   21.24 % 
Markdown                 7 hrs 46 mins       ████░░░░░░░░░░░░░░░░░░░░░   15.20 % 
Bash                     2 hrs 48 mins       █░░░░░░░░░░░░░░░░░░░░░░░░   05.49 % 

💻 Operating System: 
WSL                      42 hrs 37 mins      █████████████████████░░░░   83.42 % 
Mac                      8 hrs 28 mins       ████░░░░░░░░░░░░░░░░░░░░░   16.58 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     9 repos             ████████████░░░░░░░░░░░░░   50.00 % 
JavaScript               4 repos             ██████░░░░░░░░░░░░░░░░░░░   22.22 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   16.67 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.56 % 
Batchfile                1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.56 % 
```




 Last Updated on 16/11/2025 18:39:55 UTC
<!--END_SECTION:waka-->
