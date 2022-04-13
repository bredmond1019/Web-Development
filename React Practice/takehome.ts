type OptionTuple = [string, string];

class Languages {
  static all(): OptionTuple[] {
    // assume this is imported from an external file
    return [
      ["de", "German"],
      ["el", "Greek"],
      ["en", "English"],
      ["es", "Spanish"],
      ["fr", "French"],
      ["pt", "Portuguese"],
      ["it", "Atalian"],
      ["tr", "Turkish"],
      ["ja", "Japanese"],
      ["ar", "Arabic"],
    ];
  }
}

class Component {
  public static render(): void {
    console.log("[Component]");
  }
}

class PageTitle extends Component {
  public static render(): void {
    console.log("--- Demo Page ---");
  }
}

abstract class Dropdown extends Component {
  protected static inputName(): string {
    return "dropdown";
  }

  protected static asArray(): OptionTuple[] {
    return [];
  }

  public static render(): void {
    console.log(`<select name="${this.inputName()}">`);
    for (var l of this.asArray()) {
      console.log(` <option value="${l[0]}">${l[1]}</option>`);
    }
    console.log("</select>");
  }
}

class PrimaryLangDropdown extends Dropdown {
  protected static inputName(): string {
    return "primary_language";
  }
  protected static asArray(): OptionTuple[] {
    const common_languages: OptionTuple[] = [
      ["en", "English"],
      ["es", "Spanish"],
      ["fr", "French"],
      ["de", "German"],
      ["--", "-------"],
    ];

    const common_abbreviations: string[] = common_languages.map(
      (elem) => elem[0]
    );

    const remaining_languages: OptionTuple[] = Languages.all().filter(
      (elem) => common_abbreviations.indexOf(elem[0]) === -1
    );

    return common_languages.concat(
      remaining_languages.sort((a, b) => (a[1] > b[1] ? 1 : -1))
    );
  }
}

/* ---------------------------------------*/

const components = [PageTitle, PrimaryLangDropdown];
components.forEach((c) => c.render());
