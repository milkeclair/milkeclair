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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C276%20hrs%209%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-484.93%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                1088 commits        █████░░░░░░░░░░░░░░░░░░░░   21.43 % 
🌆 Daytime                1188 commits        ██████░░░░░░░░░░░░░░░░░░░   23.40 % 
🌃 Evening                1540 commits        ████████░░░░░░░░░░░░░░░░░   30.33 % 
🌙 Night                  1261 commits        ██████░░░░░░░░░░░░░░░░░░░   24.84 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   708 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.95 % 
Tuesday                  726 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.30 % 
Wednesday                534 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.52 % 
Thursday                 658 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.96 % 
Friday                   870 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.14 % 
Saturday                 556 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.95 % 
Sunday                   1025 commits        █████░░░░░░░░░░░░░░░░░░░░   20.19 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
TypeScript               28 hrs 42 mins      ████████████░░░░░░░░░░░░░   48.01 % 
Markdown                 25 hrs 31 mins      ███████████░░░░░░░░░░░░░░   42.68 % 
Bash                     1 hr 31 mins        █░░░░░░░░░░░░░░░░░░░░░░░░   02.56 % 
JavaScript               53 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   01.48 % 
Text                     51 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   01.45 % 

💻 Operating System: 
WSL                      59 hrs 48 mins      █████████████████████████   100.00 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     9 repos             ████████████░░░░░░░░░░░░░   47.37 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.79 % 
JavaScript               3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.79 % 
TypeScript               2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   10.53 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
```




 Last Updated on 08/04/2026 18:53:31 UTC
<!--END_SECTION:waka-->
