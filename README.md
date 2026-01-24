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
![Code Time](http://img.shields.io/badge/Code%20Time-1%2C949%20hrs%2028%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-388.56%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                922 commits         █████░░░░░░░░░░░░░░░░░░░░   21.67 % 
🌆 Daytime                967 commits         ██████░░░░░░░░░░░░░░░░░░░   22.73 % 
🌃 Evening                1281 commits        ████████░░░░░░░░░░░░░░░░░   30.11 % 
🌙 Night                  1084 commits        ██████░░░░░░░░░░░░░░░░░░░   25.48 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   571 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.42 % 
Tuesday                  601 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.13 % 
Wednesday                478 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.24 % 
Thursday                 573 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.47 % 
Friday                   760 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.87 % 
Saturday                 422 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   09.92 % 
Sunday                   849 commits         █████░░░░░░░░░░░░░░░░░░░░   19.96 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Ruby                     7 hrs 49 mins       ██████████████░░░░░░░░░░░   57.68 % 
TypeScript               5 hrs 16 mins       ██████████░░░░░░░░░░░░░░░   38.88 % 
Markdown                 14 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   01.78 % 
Bash                     12 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   01.57 % 
YAML                     0 secs              ░░░░░░░░░░░░░░░░░░░░░░░░░   00.05 % 

💻 Operating System: 
WSL                      13 hrs 5 mins       ████████████████████████░   96.50 % 
Mac                      28 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   03.50 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     10 repos            ████████████░░░░░░░░░░░░░   50.00 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.00 % 
JavaScript               3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.00 % 
TypeScript               2 repos             ██░░░░░░░░░░░░░░░░░░░░░░░   10.00 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.00 % 
```




 Last Updated on 24/01/2026 18:43:03 UTC
<!--END_SECTION:waka-->
