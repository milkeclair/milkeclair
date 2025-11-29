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
![Code Time](http://img.shields.io/badge/Code%20Time-1%2C704%20hrs%2034%20mins-blue)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-380.4%20thousand%20lines%20of%20code-blue)

**I'm a Night 🦉** 

```text
🌞 Morning                931 commits         ██████░░░░░░░░░░░░░░░░░░░   22.06 % 
🌆 Daytime                929 commits         ██████░░░░░░░░░░░░░░░░░░░   22.01 % 
🌃 Evening                1272 commits        ████████░░░░░░░░░░░░░░░░░   30.14 % 
🌙 Night                  1088 commits        ██████░░░░░░░░░░░░░░░░░░░   25.78 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   569 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.48 % 
Tuesday                  597 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.15 % 
Wednesday                464 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.00 % 
Thursday                 572 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.55 % 
Friday                   767 commits         █████░░░░░░░░░░░░░░░░░░░░   18.18 % 
Saturday                 433 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.26 % 
Sunday                   818 commits         █████░░░░░░░░░░░░░░░░░░░░   19.38 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Bash                     20 hrs 45 mins      ███████████░░░░░░░░░░░░░░   42.63 % 
Ruby                     16 hrs 26 mins      ████████░░░░░░░░░░░░░░░░░   33.77 % 
Markdown                 5 hrs 10 mins       ███░░░░░░░░░░░░░░░░░░░░░░   10.63 % 
Other                    3 hrs 3 mins        ██░░░░░░░░░░░░░░░░░░░░░░░   06.28 % 
TypeScript               2 hrs 39 mins       █░░░░░░░░░░░░░░░░░░░░░░░░   05.44 % 

💻 Operating System: 
WSL                      43 hrs 11 mins      ██████████████████████░░░   88.72 % 
Mac                      5 hrs 29 mins       ███░░░░░░░░░░░░░░░░░░░░░░   11.28 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     10 repos            █████████████░░░░░░░░░░░░   52.63 % 
JavaScript               4 repos             █████░░░░░░░░░░░░░░░░░░░░   21.05 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.79 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
Batchfile                1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
```




 Last Updated on 29/11/2025 18:41:09 UTC
<!--END_SECTION:waka-->
