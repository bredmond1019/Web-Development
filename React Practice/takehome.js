var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var Languages = /** @class */ (function () {
    function Languages() {
    }
    Languages.all = function () {
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
    };
    return Languages;
}());
var Component = /** @class */ (function () {
    function Component() {
    }
    Component.render = function () {
        console.log("[Component]");
    };
    return Component;
}());
var PageTitle = /** @class */ (function (_super) {
    __extends(PageTitle, _super);
    function PageTitle() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    PageTitle.render = function () {
        console.log("--- Demo Page ---");
    };
    return PageTitle;
}(Component));
var Dropdown = /** @class */ (function (_super) {
    __extends(Dropdown, _super);
    function Dropdown() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Dropdown.inputName = function () {
        return "dropdown";
    };
    Dropdown.asArray = function () {
        return [];
    };
    Dropdown.render = function () {
        console.log("<select name=\"".concat(this.inputName(), "\">"));
        for (var _i = 0, _a = this.asArray(); _i < _a.length; _i++) {
            var l = _a[_i];
            console.log(" <option value=\"".concat(l[0], "\">").concat(l[1], "</option>"));
        }
        console.log("</select>");
    };
    return Dropdown;
}(Component));
var PrimaryLangDropdown = /** @class */ (function (_super) {
    __extends(PrimaryLangDropdown, _super);
    function PrimaryLangDropdown() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    PrimaryLangDropdown.inputName = function () {
        return "primary_language";
    };
    PrimaryLangDropdown.asArray = function () {
        var common_languages = [
            ["en", "English"],
            ["es", "Spanish"],
            ["fr", "French"],
            ["de", "German"],
            ["--", "-------"],
        ];
        var common_abbreviations = common_languages.map(function (elem) { return elem[0]; });
        var remaining_languages = Languages.all().filter(function (elem) { return common_abbreviations.indexOf(elem[0]) === -1; });
        return common_languages.concat(remaining_languages.sort(function (a, b) { return (a[1] > b[1] ? 1 : -1); }));
    };
    return PrimaryLangDropdown;
}(Dropdown));
/* ---------------------------------------*/
var components = [PageTitle, PrimaryLangDropdown];
components.forEach(function (c) { return c.render(); });
