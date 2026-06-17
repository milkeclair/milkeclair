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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C568%20hrs%2033%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-613.44%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                1370 commits        █████░░░░░░░░░░░░░░░░░░░░   21.06 % 
🌆 Daytime                1554 commits        ██████░░░░░░░░░░░░░░░░░░░   23.89 % 
🌃 Evening                1885 commits        ███████░░░░░░░░░░░░░░░░░░   28.98 % 
🌙 Night                  1696 commits        ███████░░░░░░░░░░░░░░░░░░   26.07 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   831 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.77 % 
Tuesday                  899 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.82 % 
Wednesday                641 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   09.85 % 
Thursday                 823 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.65 % 
Friday                   1204 commits        █████░░░░░░░░░░░░░░░░░░░░   18.51 % 
Saturday                 729 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.21 % 
Sunday                   1378 commits        █████░░░░░░░░░░░░░░░░░░░░   21.18 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Java                     17 hrs 26 mins      █████████████████░░░░░░░░   68.25 % 
Markdown                 2 hrs 52 mins       ███░░░░░░░░░░░░░░░░░░░░░░   11.25 % 
Other                    1 hr 32 mins        ██░░░░░░░░░░░░░░░░░░░░░░░   06.03 % 
Ruby                     1 hr                █░░░░░░░░░░░░░░░░░░░░░░░░   03.95 % 
Image (svg)              59 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   03.87 % 

💻 Operating System: 
WSL                      24 hrs 23 mins      ████████████████████████░   95.47 % 
Mac                      1 hr 9 mins         █░░░░░░░░░░░░░░░░░░░░░░░░   04.53 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     9 repos             ████████████░░░░░░░░░░░░░   47.37 % 
TypeScript               2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   10.53 % 
Shell                    2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   10.53 % 
Java                     1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
```




 Last Updated on 17/06/2026 19:18:58 UTC
<!--END_SECTION:waka-->
