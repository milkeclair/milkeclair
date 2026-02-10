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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C025%20hrs%2021%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-396.88%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                955 commits         █████░░░░░░░░░░░░░░░░░░░░   21.15 % 
🌆 Daytime                1056 commits        ██████░░░░░░░░░░░░░░░░░░░   23.38 % 
🌃 Evening                1368 commits        ████████░░░░░░░░░░░░░░░░░   30.29 % 
🌙 Night                  1137 commits        ██████░░░░░░░░░░░░░░░░░░░   25.18 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   643 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.24 % 
Tuesday                  651 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.42 % 
Wednesday                501 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.09 % 
Thursday                 599 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.26 % 
Friday                   771 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.07 % 
Saturday                 470 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.41 % 
Sunday                   881 commits         █████░░░░░░░░░░░░░░░░░░░░   19.51 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Markdown                 13 hrs 22 mins      ████████░░░░░░░░░░░░░░░░░   30.18 % 
TypeScript               12 hrs 51 mins      ███████░░░░░░░░░░░░░░░░░░   29.03 % 
Ruby                     12 hrs 25 mins      ███████░░░░░░░░░░░░░░░░░░   28.04 % 
JSONiq                   2 hrs 23 mins       █░░░░░░░░░░░░░░░░░░░░░░░░   05.40 % 
SSH Config               37 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   01.39 % 

💻 Operating System: 
WSL                      44 hrs 18 mins      █████████████████████████   100.00 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     10 repos            ████████████░░░░░░░░░░░░░   50.00 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.00 % 
JavaScript               3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.00 % 
TypeScript               2 repos             ██░░░░░░░░░░░░░░░░░░░░░░░   10.00 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.00 % 
```




 Last Updated on 10/02/2026 18:49:06 UTC
<!--END_SECTION:waka-->
