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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C094%20hrs%2033%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-443.64%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                1059 commits        █████░░░░░░░░░░░░░░░░░░░░   21.91 % 
🌆 Daytime                1114 commits        ██████░░░░░░░░░░░░░░░░░░░   23.05 % 
🌃 Evening                1457 commits        ████████░░░░░░░░░░░░░░░░░   30.15 % 
🌙 Night                  1203 commits        ██████░░░░░░░░░░░░░░░░░░░   24.89 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   696 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.40 % 
Tuesday                  692 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.32 % 
Wednesday                518 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.72 % 
Thursday                 635 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.14 % 
Friday                   835 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.28 % 
Saturday                 512 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.59 % 
Sunday                   945 commits         █████░░░░░░░░░░░░░░░░░░░░   19.55 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Bash                     24 hrs 47 mins      ███████████████████░░░░░░   77.35 % 
TypeScript               2 hrs 25 mins       ██░░░░░░░░░░░░░░░░░░░░░░░   07.57 % 
Ruby                     1 hr 31 mins        █░░░░░░░░░░░░░░░░░░░░░░░░   04.76 % 
Markdown                 1 hr 29 mins        █░░░░░░░░░░░░░░░░░░░░░░░░   04.68 % 
Other                    58 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   03.04 % 

💻 Operating System: 
WSL                      31 hrs 47 mins      █████████████████████████   99.22 % 
Mac                      14 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   00.78 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     10 repos            ████████████░░░░░░░░░░░░░   50.00 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.00 % 
JavaScript               3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.00 % 
TypeScript               2 repos             ██░░░░░░░░░░░░░░░░░░░░░░░   10.00 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.00 % 
```




 Last Updated on 28/02/2026 18:44:58 UTC
<!--END_SECTION:waka-->
