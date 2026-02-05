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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C010%20hrs%209%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-391.90%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                935 commits         █████░░░░░░░░░░░░░░░░░░░░   21.65 % 
🌆 Daytime                986 commits         ██████░░░░░░░░░░░░░░░░░░░   22.83 % 
🌃 Evening                1299 commits        ████████░░░░░░░░░░░░░░░░░   30.08 % 
🌙 Night                  1099 commits        ██████░░░░░░░░░░░░░░░░░░░   25.45 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   600 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.89 % 
Tuesday                  605 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.01 % 
Wednesday                492 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.39 % 
Thursday                 578 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.38 % 
Friday                   760 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.60 % 
Saturday                 429 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   09.93 % 
Sunday                   855 commits         █████░░░░░░░░░░░░░░░░░░░░   19.80 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Ruby                     18 hrs 13 mins      █████████░░░░░░░░░░░░░░░░   37.30 % 
Markdown                 13 hrs 31 mins      ███████░░░░░░░░░░░░░░░░░░   27.69 % 
TypeScript               12 hrs 52 mins      ███████░░░░░░░░░░░░░░░░░░   26.35 % 
SSH Config               58 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   02.00 % 
Other                    45 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   01.54 % 

💻 Operating System: 
WSL                      48 hrs 50 mins      █████████████████████████   100.00 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     10 repos            ████████████░░░░░░░░░░░░░   50.00 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.00 % 
JavaScript               3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.00 % 
TypeScript               2 repos             ██░░░░░░░░░░░░░░░░░░░░░░░   10.00 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.00 % 
```




 Last Updated on 05/02/2026 18:46:54 UTC
<!--END_SECTION:waka-->
