Web [tkalci.cz](http://tkalci.cz) je generován nástrojem 
[Pelican](http://blog.getpelican.com/), který
konvertuje obsah sepsaný v Markdown syntaxi na kolekci statických stránek. 

* [Obsah]()
  * [Formát souborů]()
  * [Pozvánky]()
  * [Zápisy]()
  * [Statické stránky]()
  * [Obrázky]()
* [Jak můžete pomoct]()
  * [Úpravy obsahu]()
  * [Rozšiřování funkcionality]()
* [Docker]()
  * [Build]()
  * [Vygenerování statického obsahu]()
* [Šablony]()

## Obsah

Veškerý obsah je uložen ve složce `content/`:

* `blog/pozvanky/` -- tady se ukládají pozvánky na srazy. V zářné
  budoucnosti pak některá dobrá duše napíše kód, který její obsah automaticky
  překlopí na služby [srazy.info](http://srazy.info/tkalci-na-webu) a 
  [lanyrd.com](http://lanyrd.com/series/tkalci-na-webu/). Než se tak opravdu 
  stane, budem do zmíněných služeb pozvánky kopírovat manuálně.
* `blog/zapisy/` -- vystavení videí ze srazu vždycky chvíli trvá a ne každý si
  najde 3 hodiny na jejich zpětné shlédnutí. Proto budeme dle možností pořizovat 
  ze srazů i stručný textový zápis, jehož autorem může být kdokoli z přítomných. 
  Zápis by měl být shrnutím toho, co na srazu zaznělo, ideálně doplněno o
  relevantní odkazy, slajdy a posléze i videa.
* `blog/srumec/` -- krátké glosy o zajímavostech a novinkách okolo webového
  vývoje.
* `stranky/` -- víceméně statický obsah webu do kterého nebude potřeba příliš
  často zasahovat.

### Formát souborů

Obsah webu je vytvářen ze souborů, které musí:

* být uloženy v konkrétních adresářích
* být pojmenovány podle předem dané formy
* být sepsány v [Markdown](https://daringfireball.net/projects/markdown/syntax) 
  syntaxi doplněné sadou metadat 

Každý soubor je rozdělen na 2 části: metadata v úvodu a samotný obsah. Např.:

    Title: Nádherný titulek
    Date: 2015-09-19 08:23

    První obsahový odstavec.

    Druhý obsahový odstavec.

Metadata v úvodu, podle kterých *Pelican* pozná kam obsah zařadit, jakou
šablonu použít, apod., mají formu `Klic: Hodnota`. *Pelican* definuje sadu
[standardních klíčů](http://docs.getpelican.com/en/3.6.3/content.html#file-metadata), 
tkalcovská implementace pak přidává pár nových (popsáno níže).

### Pozvánky

Kam pozvánky ukládat:

    content/blog/pozvanky/<cislo>_<jmeno>.md

`<cislo>` je pořadové číslo srazu, `<jmeno>` je titulek srazu přepsaný do malých
písmen bez diakritiky, mezery nahrazeny za znak `_`.

Metadata:

    Title: Název srazu
    Date: Datum konání srazu, např. 2015-06-09 18:00
    Tags: Tagy vyjadřující témata srazu, např. expressjs, nodejs
    Summary: Jednovětný popis srazu

### Zápisy

Kam zápisy ukládat:

    content/blog/zapisy/<cislo>_<jmeno>.md

`<cislo>` je pořadové číslo srazu, `<jmeno>` je titulek srazu přepsaný do malých
písmen bez diakritiky, mezery nahrazeny za znak `_`.

Metadata:

    Title: Název srazu
    Date: Datum konání srazu, např. 2015-06-09 18:00
    Tags: Tagy vyjadřující témata srazu, např. expressjs, nodejs
    Authors: Jméno autora (toho, kdo zápis vytváří)
    Summary: Jednovětný popis srazu

Metadata jsou shodná s těmi, která jsou uvedena u pozvánky. Nově se zde vyskytuje
pouze klíč `Authors`, do kterého je možné uložit jména lidí (oddělena čárkami), 
kteří zápis pořídili. *Pelican* pak umí automaticky pro každého člověka vytvořit
profilovou stránku se seznamem obsahu, které dotyčný na web vystavil.

### Statické stránky

Kam stránky ukládat:

    content/stranky/<jmeno>.md

Metadata:

    Title: Jméno stránky
    Summary: Jednovětný popis stránky.
    Tags: Tagy vyjadřující obsah stránky, např. books
    Template: Jméno šablony, nepovinný parametr
    FrontImage: Cesta k úvodnímu obrázku, nepovinný parametr

Význam jednotlivých klíčů je podobný jako u zápisů či pozvánek. Za komentář stojí:

* `Template` -- každá stránka se generuje prostřednictvím některé ze šablon
  z adresáře `templates/templates/`. Defaultně si *Pelican* šáhne po šabloně `page`,
  ale právě s pomocí klíče `Template` je možné tuto volbu přebít.
* `FrontImage` -- každá ze stránek může být uvozena obrázkem roztaženým přes
  celou šířku stránky. Stačí do tohoto klíče uložit cestu k obrázku z adresáře
  `image`, např. `FrontImage: /images/img03.jpg`

Většina stránek má statický charakter, a nebude vznikat velká potřeba jejich 
obsah často měnit. Vyjímkou je soubor `content/blog/knihovna.md`, ve kterém
udržujeme seznam sdílených knih a lidí, kteří si některou z nich půjčili.  

### Obrázky

Do složky `content/images/` je možné ukládat obrázky, na které se pak dá 
odkazovat z obsahových Markdown souborů (např. prostřednictvím meta klíče 
`FrontImage` nebo standardně 
[Markdown syntaxí pro obrázky](https://daringfireball.net/projects/markdown/syntax#img)).

Cesta k obrázku se zadává ve tvaru `/images/<jmeno>`.


## Jak můžete pomoct

1. Udržovat aktuální obsah
2. Rozšiřovat funkcionalitu *Pelicana* nebo vytvořit podpůrné skripty

### Úpravy obsahu

Jsme na [GitHubu](), obsah tkalcovského webu je přístupný komukoli. Pokud 
naleznete nějakou nepřesnost, budete chtít pořídit zápis s uskutečněného srazu, 
aktualizovat informace v knihovně, či upravit/přidat obsah jakékoliv stránky, 
směle do toho! Stačí když pošlete pull request s vaší úpravou.

### Rozšiřování funkcionality

V issues naleznete seznam věcí, které by bylo dobré někdy pro naše stránky 
zrealizovat.


## Docker

Pro snadnější generování výsledného statického webu používáme Docker. Pokud
budeš chtít tkalcovský web vygenerovat u sebe v počítači, naklonuj si tento
repozitář a postupuj podle následujících instrukcí.

Poznámka: každý docker image je otagován, aby se v něm lidi lépe vyznali.
Já jsem jej nazval `msgre/common:tkalci`, kde `msgre` je mé uživatelské jméno
na Docker hubu, `common` je obecný repozitář do kterého ukládám image pro
některé své projekty, a `tkalci` je tag. Pokud budeš buildit svou variantu image,
zvol nějaké jiné jméno.

### Build

    docker build -t msgre/common:tkalci .

Poznámka: pokud nechceš image buildit, můžeš si jej stáhnout z repozitáře
na Docker hubu:

    docker pull msgre/common:tkalci


### Vygenerování statického obsahu

Pro jednorázové překlopení obsahu popsaného v adresáři [`content/`](content)
stačí zavolat:

    docker run -ti -v $PWD:/src --rm msgre/common:tkalci html

Pokud ale průběžně ladíš obsah a kontroluješ jeho podobu, šáhni po utilitě
fswatch a spusť:

    # continuous build of output HTML files:
    fswatch --include="\.md" -o $PWD/content | xargs -n1 -I{} docker run -i -v $PWD:/src --rm msgre/common:tkalci html

Tento příkaz bude sledovat Markdown soubory a při jakékoliv změně automaticky 
spustí kompilaci do HTML.

Výsledkem obou výše uvedených příkazů je statický web uložený v adresáři 
`output/`. Ten se pak 1:1 překlápí přes FTP na hosting. 

Pokud potřebuješ zkontrolovat podobu výsledného webu u sebe na počítači, 
vlez do adresáře `output/` a spusť příkaz:

    python -m SimpleHTTPServer

Otevři webový prohlížeč a navštiv URL adresu `http://localhost:8000/`.

## Šablony

Tkalcovský web používá legálně zakoupenou šablonu 
[Snowbird](http://themeforest.net/item/snowbird-personal-blog-html-template/12323835)
z webu [themeforest](http://themeforest.net/).

**Obsah adresáře [`templates/`](templates) není určen pro další šíření a slouží
výhradně pro web [tkalci.cz](http://tkalci.cz)!**
