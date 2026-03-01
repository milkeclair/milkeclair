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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C102%20hrs%2021%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-430.29%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                976 commits         █████░░░░░░░░░░░░░░░░░░░░   20.67 % 
🌆 Daytime                1133 commits        ██████░░░░░░░░░░░░░░░░░░░   23.99 % 
🌃 Evening                1429 commits        ████████░░░░░░░░░░░░░░░░░   30.26 % 
🌙 Night                  1184 commits        ██████░░░░░░░░░░░░░░░░░░░   25.07 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   645 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.66 % 
Tuesday                  685 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.51 % 
Wednesday                514 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.89 % 
Thursday                 622 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.17 % 
Friday                   813 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.22 % 
Saturday                 501 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.61 % 
Sunday                   942 commits         █████░░░░░░░░░░░░░░░░░░░░   19.95 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Bash                     34 hrs 45 mins      ████████████████████░░░░░   81.33 % 
TypeScript               2 hrs 25 mins       █░░░░░░░░░░░░░░░░░░░░░░░░   05.68 % 
Markdown                 2 hrs 12 mins       █░░░░░░░░░░░░░░░░░░░░░░░░   05.15 % 
Ruby                     1 hr 31 mins        █░░░░░░░░░░░░░░░░░░░░░░░░   03.57 % 
Other                    58 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   02.28 % 

💻 Operating System: 
WSL                      42 hrs 29 mins      █████████████████████████   99.42 % 
Mac                      14 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   00.58 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     9 repos             ████████████░░░░░░░░░░░░░   47.37 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.79 % 
JavaScript               3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.79 % 
TypeScript               2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   10.53 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
```




 Last Updated on 01/03/2026 18:44:33 UTC
<!--END_SECTION:waka-->
