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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C620%20hrs%2053%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-537.79%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                1266 commits        █████░░░░░░░░░░░░░░░░░░░░   20.82 % 
🌆 Daytime                1460 commits        ██████░░░░░░░░░░░░░░░░░░░   24.01 % 
🌃 Evening                1710 commits        ███████░░░░░░░░░░░░░░░░░░   28.12 % 
🌙 Night                  1644 commits        ███████░░░░░░░░░░░░░░░░░░   27.04 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   745 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.25 % 
Tuesday                  842 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.85 % 
Wednesday                607 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   09.98 % 
Thursday                 768 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.63 % 
Friday                   1153 commits        █████░░░░░░░░░░░░░░░░░░░░   18.96 % 
Saturday                 676 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.12 % 
Sunday                   1289 commits        █████░░░░░░░░░░░░░░░░░░░░   21.20 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Bash                     12 hrs 25 mins      █████████████████░░░░░░░░   66.05 % 
Markdown                 3 hrs 44 mins       █████░░░░░░░░░░░░░░░░░░░░   19.90 % 
TypeScript               2 hrs               ███░░░░░░░░░░░░░░░░░░░░░░   10.69 % 
JSON                     18 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   01.64 % 
Ruby                     12 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   01.10 % 

💻 Operating System: 
WSL                      18 hrs 43 mins      █████████████████████████   99.54 % 
Windows                  5 mins              ░░░░░░░░░░░░░░░░░░░░░░░░░   00.46 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     8 repos             █████████████░░░░░░░░░░░░   53.33 % 
TypeScript               2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   13.33 % 
Java                     1 repo              ██░░░░░░░░░░░░░░░░░░░░░░░   06.67 % 
Shell                    1 repo              ██░░░░░░░░░░░░░░░░░░░░░░░   06.67 % 
CSS                      1 repo              ██░░░░░░░░░░░░░░░░░░░░░░░   06.67 % 
```




 Last Updated on 04/07/2026 18:48:11 UTC
<!--END_SECTION:waka-->
