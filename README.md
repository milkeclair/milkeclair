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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C213%20hrs%2045%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-434.19%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                984 commits         █████░░░░░░░░░░░░░░░░░░░░   20.68 % 
🌆 Daytime                1133 commits        ██████░░░░░░░░░░░░░░░░░░░   23.81 % 
🌃 Evening                1441 commits        ████████░░░░░░░░░░░░░░░░░   30.28 % 
🌙 Night                  1201 commits        ██████░░░░░░░░░░░░░░░░░░░   25.24 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   652 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.70 % 
Tuesday                  685 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.39 % 
Wednesday                520 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.93 % 
Thursday                 630 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.24 % 
Friday                   814 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.10 % 
Saturday                 514 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.80 % 
Sunday                   944 commits         █████░░░░░░░░░░░░░░░░░░░░   19.84 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Ruby                     20 hrs 48 mins      ███████████████████░░░░░░   74.58 % 
Markdown                 5 hrs 39 mins       █████░░░░░░░░░░░░░░░░░░░░   20.27 % 
JSON                     33 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   02.01 % 
TypeScript               15 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   00.95 % 
Terraform                11 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   00.68 % 

💻 Operating System: 
WSL                      26 hrs 31 mins      ████████████████████████░   95.05 % 
Mac                      1 hr 21 mins        █░░░░░░░░░░░░░░░░░░░░░░░░   04.89 % 
Windows                  1 min               ░░░░░░░░░░░░░░░░░░░░░░░░░   00.06 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     9 repos             ████████████░░░░░░░░░░░░░   47.37 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.79 % 
JavaScript               3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.79 % 
TypeScript               2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   10.53 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
```




 Last Updated on 01/04/2026 18:47:48 UTC
<!--END_SECTION:waka-->
