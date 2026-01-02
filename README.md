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
![Code Time](http://img.shields.io/badge/Code%20Time-1%2C900%20hrs%2023%20mins-blue)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-387.28%20thousand%20lines%20of%20code-blue)

**I'm a Night 🦉** 

```text
🌞 Morning                922 commits         █████░░░░░░░░░░░░░░░░░░░░   21.70 % 
🌆 Daytime                967 commits         ██████░░░░░░░░░░░░░░░░░░░   22.76 % 
🌃 Evening                1278 commits        ████████░░░░░░░░░░░░░░░░░   30.08 % 
🌙 Night                  1082 commits        ██████░░░░░░░░░░░░░░░░░░░   25.46 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   570 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.41 % 
Tuesday                  600 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.12 % 
Wednesday                478 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.25 % 
Thursday                 571 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.44 % 
Friday                   759 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.86 % 
Saturday                 422 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   09.93 % 
Sunday                   849 commits         █████░░░░░░░░░░░░░░░░░░░░   19.98 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Ruby                     21 hrs 30 mins      ████████████████████░░░░░   80.10 % 
JavaScript               4 hrs 14 mins       ████░░░░░░░░░░░░░░░░░░░░░   15.81 % 
ERB                      44 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   02.73 % 
TypeScript               13 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   00.81 % 
YAML                     7 mins              ░░░░░░░░░░░░░░░░░░░░░░░░░   00.45 % 

💻 Operating System: 
WSL                      26 hrs 46 mins      █████████████████████████   99.65 % 
Mac                      5 mins              ░░░░░░░░░░░░░░░░░░░░░░░░░   00.35 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     10 repos            ████████████░░░░░░░░░░░░░   47.62 % 
JavaScript               4 repos             █████░░░░░░░░░░░░░░░░░░░░   19.05 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   14.29 % 
TypeScript               2 repos             ██░░░░░░░░░░░░░░░░░░░░░░░   09.52 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   04.76 % 
```




 Last Updated on 02/01/2026 18:43:58 UTC
<!--END_SECTION:waka-->
