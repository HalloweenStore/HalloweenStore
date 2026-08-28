#!/usr/bin/env python3
"""Generate iPhone Shortcuts (.shortcut) files for the fitness plan."""

from __future__ import annotations

import plistlib
import uuid
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent / "shortcuts"


def new_uuid() -> str:
    return str(uuid.uuid4()).upper()


def action_id(name: str) -> str:
    return f"is.workflow.actions.{name}"


def base_workflow(name: str, actions: list[dict]) -> dict:
    return {
        "WFWorkflowActions": actions,
        "WFWorkflowClientRelease": "18.0",
        "WFWorkflowClientVersion": "2702.0.4",
        "WFWorkflowHasOutputFallback": False,
        "WFWorkflowHasShortcutInputVariables": False,
        "WFWorkflowIcon": {
            "WFWorkflowIconGlyphNumber": 59446,
            "WFWorkflowIconStartColor": 4292093695,
        },
        "WFWorkflowImportQuestions": [],
        "WFWorkflowInputContentItemClasses": [
            "WFAppStoreAppContentItem",
            "WFArticleContentItem",
            "WFContactContentItem",
            "WFDateContentItem",
            "WFEmailAddressContentItem",
            "WFGenericFileContentItem",
            "WFImageContentItem",
            "WFiTunesProductContentItem",
            "WFLocationContentItem",
            "WFDCMapsLinkContentItem",
            "WFAVAssetContentItem",
            "WFPDFContentItem",
            "WFPhoneNumberContentItem",
            "WFRichTextContentItem",
            "WFSafariWebPageContentItem",
            "WFStringContentItem",
            "WFURLContentItem",
        ],
        "WFWorkflowMinimumClientVersion": 900,
        "WFWorkflowMinimumClientVersionString": "900",
        "WFWorkflowName": name,
        "WFWorkflowOutputContentItemClasses": [],
        "WFWorkflowTypes": [],
    }


def alert_action(title: str, message: str) -> dict:
    return {
        "WFWorkflowActionIdentifier": action_id("alert"),
        "WFWorkflowActionParameters": {
            "WFAlertActionTitle": title,
            "WFAlertActionMessage": message,
            "WFAlertActionCancelButtonShown": False,
        },
    }


def date_action(action_uuid: str | None = None) -> dict:
    params: dict = {"WFDateActionMode": "Current Date"}
    if action_uuid:
        params["UUID"] = action_uuid
    return {
        "WFWorkflowActionIdentifier": action_id("date"),
        "WFWorkflowActionParameters": params,
    }


def format_date_action(source_uuid: str, action_uuid: str | None = None) -> dict:
    params: dict = {
        "WFDateFormatStyle": "Custom",
        "WFDateFormat": "EEEE",
        "WFTimeFormatStyle": "None",
        "WFInput": {
            "Value": {
                "OutputName": "Date",
                "OutputUUID": source_uuid,
                "Type": "ActionOutput",
            },
            "WFSerializationType": "WFTextTokenAttachment",
        },
    }
    if action_uuid:
        params["UUID"] = action_uuid
    return {
        "WFWorkflowActionIdentifier": action_id("format.date"),
        "WFWorkflowActionParameters": params,
    }


def variable_input(source_uuid: str, output_name: str = "Formatted Date") -> dict:
    return {
        "Type": "Variable",
        "Variable": {
            "Value": {
                "OutputName": output_name,
                "OutputUUID": source_uuid,
                "Type": "ActionOutput",
            },
            "WFSerializationType": "WFTextTokenAttachment",
        },
    }


def if_start(group_id: str, source_uuid: str, value: str) -> dict:
    return {
        "WFWorkflowActionIdentifier": action_id("conditional"),
        "WFWorkflowActionParameters": {
            "GroupingIdentifier": group_id,
            "WFControlFlowMode": 0,
            "WFCondition": 4,
            "WFConditionalActionString": value,
            "WFInput": variable_input(source_uuid),
        },
    }


def else_if(group_id: str, source_uuid: str, value: str) -> dict:
    return {
        "WFWorkflowActionIdentifier": action_id("conditional"),
        "WFWorkflowActionParameters": {
            "GroupingIdentifier": group_id,
            "WFControlFlowMode": 1,
            "WFCondition": 4,
            "WFConditionalActionString": value,
            "WFInput": variable_input(source_uuid),
        },
    }


def else_branch(group_id: str) -> dict:
    return {
        "WFWorkflowActionIdentifier": action_id("conditional"),
        "WFWorkflowActionParameters": {
            "GroupingIdentifier": group_id,
            "WFControlFlowMode": 1,
        },
    }


def end_if(group_id: str) -> dict:
    return {
        "WFWorkflowActionIdentifier": action_id("conditional"),
        "WFWorkflowActionParameters": {
            "GroupingIdentifier": group_id,
            "WFControlFlowMode": 2,
        },
    }


def menu_start(group_id: str, prompt: str, items: list[str]) -> dict:
    return {
        "WFWorkflowActionIdentifier": action_id("choosefrommenu"),
        "WFWorkflowActionParameters": {
            "GroupingIdentifier": group_id,
            "WFControlFlowMode": 0,
            "WFMenuPrompt": prompt,
            "WFMenuItems": items,
        },
    }


def menu_case(group_id: str, title: str) -> dict:
    return {
        "WFWorkflowActionIdentifier": action_id("choosefrommenu"),
        "WFWorkflowActionParameters": {
            "GroupingIdentifier": group_id,
            "WFControlFlowMode": 1,
            "WFMenuItemTitle": title,
        },
    }


def menu_end(group_id: str) -> dict:
    return {
        "WFWorkflowActionIdentifier": action_id("choosefrommenu"),
        "WFWorkflowActionParameters": {
            "GroupingIdentifier": group_id,
            "WFControlFlowMode": 2,
        },
    }


WORKOUTS: dict[str, str] = {
    "Pazartesi": """🏋️ GÜÇ ANTRENMANI A

Isınma: 5 dk yürüyüş + 3 dk eklem açıcı

1. Goblet squat — 3×10-12 (90 sn)
2. Şınav — 3×8-12
3. Romanian deadlift — 3×10
4. Dambıl row — 3×10/kol
5. Plank — 3×20-30 sn
6. Glute bridge — 3×12

Bitiriş: 15 dk hafif yürüyüş
RPE: 5-6 | Konuşabildiğiniz tempo!""",
    "Salı": """🚶 KARDİYO GÜNÜ (30 dk)

• 5 dk ısınma yürüyüşü
• 20 dk hızlı yürüyüş / eğimli treadmill (%3-5)
• 5 dk soğuma

Nefes kesilirse yavaşlayın.""",
    "Çarşamba": """🏋️ GÜÇ ANTRENMANI B

1. Adım çıkma — 3×10/ayak
2. Dambıl omuz press — 3×10
3. Lat pulldown / band row — 3×12
4. Lunges — 3×8/ayak
5. Dead bug — 3×10/yan
6. Calf raise — 3×15

Bitiriş: 15 dk hafif yürüyüş""",
    "Perşembe": """🧘 AKTİF DİNLENME

• 20-30 dk rahat yürüyüş
veya
• 15 dk esneme / yoga

Antrenman yok — toparlanma günü.""",
    "Cuma": """🏋️ GÜÇ ANTRENMANI A

(Pazartesi ile aynı program)
Setler arası 90 sn dinlenme.""",
    "Cumartesi": """⚡ HAFİF İNTERVAL

• 5 dk ısınma
• 1 dk hızlı + 2 dk yavaş × 6-8 tur
• 5 dk soğuma

Nefes kesilirse düz yürüyüşe geç.""",
    "Pazar": """😴 TAM DİNLENME

Antrenman yok.
Kreatin 3-5g + 2,5L su + 7+ saat uyku.""",
}

DAY_ALIASES: dict[str, list[str]] = {
    "Pazartesi": ["Pazartesi", "Monday"],
    "Salı": ["Salı", "Tuesday"],
    "Çarşamba": ["Çarşamba", "Wednesday"],
    "Perşembe": ["Perşembe", "Thursday"],
    "Cuma": ["Cuma", "Friday"],
    "Cumartesi": ["Cumartesi", "Saturday"],
    "Pazar": ["Pazar", "Sunday"],
}

CREATINE_MSG = """💊 KREATİN

Doz: 3-5 gram / gün
Yemekle birlikte alın.

💧 Günde en az 2,5 litre su.
İlk haftalarda +0,5-1 kg su tutumu normaldir."""

CHECKLIST_MSG = """✅ GÜNLÜK KONTROL

□ Kreatin 3-5g
□ 2,5+ litre su
□ Antrenman tamamlandı
□ 7+ saat uyku
□ Protein 130-160g

Hedef: 72-75 kg | Haftalık -0,3-0,5 kg"""

BREATH_MSG = """🫁 NEFES KURALLARI

1. Konuşma testi — cümle kurabilmelisin
2. RPE 5-6 — nefes nefese kalma
3. Burundan nefes al
4. Set arası 90-120 sn dinlen
5. Göğüs ağrısı/baş dönmesi → DUR

178cm · 80kg · 8 haftalık program"""

WEEK_SUMMARY = """📅 HAFTALIK PROGRAM

Pzt → Güç A + yürüyüş
Sal → Kardiyo 30 dk
Çar → Güç B + yürüyüş
Per → Aktif dinlenme
Cum → Güç A + yürüyüş
Cmt → Hafif interval
Paz → Tam dinlenme

Kreatin: 3-5g/gün + bol su"""


def build_weekday_conditionals(format_uuid: str, fallback_title: str, fallback_msg: str) -> list[dict]:
    """Build if / else-if chain for each weekday (TR + EN names)."""
    actions: list[dict] = []
    group_id = new_uuid()
    first = True

    for day, aliases in DAY_ALIASES.items():
        workout = WORKOUTS[day]
        for alias in aliases:
            if first:
                actions.append(if_start(group_id, format_uuid, alias))
                first = False
            else:
                actions.append(else_if(group_id, format_uuid, alias))
            actions.append(alert_action(f"{day} — Antrenman", workout))

    actions.append(else_branch(group_id))
    actions.append(
        alert_action(
            fallback_title,
            fallback_msg,
        )
    )
    actions.append(end_if(group_id))
    return actions


def build_today_workout_shortcut() -> dict:
    date_uuid = new_uuid()
    format_uuid = new_uuid()
    actions = [
        date_action(date_uuid),
        format_date_action(date_uuid, format_uuid),
        *build_weekday_conditionals(
            format_uuid,
            "Gün Tanınamadı",
            "Telefon dilini Türkçe yapın veya 'Gün Seç' kestirmesini kullanın.\n\n"
            + WEEK_SUMMARY,
        ),
    ]
    return base_workflow("Bugünkü Antrenman", actions)


def build_day_picker_shortcut() -> dict:
    group_id = new_uuid()
    days = list(WORKOUTS.keys())
    actions = [menu_start(group_id, "Hangi günün planını görmek istiyorsun?", days)]
    for day in days:
        actions.append(menu_case(group_id, day))
        actions.append(alert_action(f"{day} — Antrenman", WORKOUTS[day]))
    actions.append(menu_end(group_id))
    return base_workflow("Gün Seç — Antrenman", actions)


def build_main_menu_shortcut() -> dict:
    group_id = new_uuid()
    items = [
        "Bugünkü antrenman",
        "Gün seç (manuel)",
        "Kreatin hatırlatma",
        "Günlük kontrol listesi",
        "Nefes kuralları",
        "Haftalık program",
    ]
    actions: list[dict] = [menu_start(group_id, "Spor Planım — 178cm / 80kg", items)]

    # Bugünkü antrenman
    date_uuid = new_uuid()
    format_uuid = new_uuid()
    actions.append(menu_case(group_id, "Bugünkü antrenman"))
    actions.extend(
        [
            date_action(date_uuid),
            format_date_action(date_uuid, format_uuid),
            *build_weekday_conditionals(format_uuid, "Gün Tanınamadı", WEEK_SUMMARY),
        ]
    )

    # Gün seç submenu
    sub_group = new_uuid()
    days = list(WORKOUTS.keys())
    actions.append(menu_case(group_id, "Gün seç (manuel)"))
    actions.append(menu_start(sub_group, "Gün seç:", days))
    for day in days:
        actions.append(menu_case(sub_group, day))
        actions.append(alert_action(day, WORKOUTS[day]))
    actions.append(menu_end(sub_group))

    extras = [
        ("Kreatin hatırlatma", "Kreatin 💊", CREATINE_MSG),
        ("Günlük kontrol listesi", "Kontrol Listesi", CHECKLIST_MSG),
        ("Nefes kuralları", "Nefes Kuralları", BREATH_MSG),
        ("Haftalık program", "Haftalık Program", WEEK_SUMMARY),
    ]
    for menu_item, title, body in extras:
        actions.append(menu_case(group_id, menu_item))
        actions.append(alert_action(title, body))

    actions.append(menu_end(group_id))
    return base_workflow("Spor Planım", actions)


def build_creatine_reminder() -> dict:
    return base_workflow("Kreatin Hatırlatıcı", [alert_action("Kreatin Zamanı 💊", CREATINE_MSG)])


def write_shortcut(workflow: dict, filename: str) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUTPUT_DIR / filename
    with open(path, "wb") as f:
        plistlib.dump(workflow, f, fmt=plistlib.FMT_BINARY)
    return path


def main() -> None:
    shortcuts = [
        (build_main_menu_shortcut(), "Spor-Planim.shortcut"),
        (build_today_workout_shortcut(), "Bugunku-Antrenman.shortcut"),
        (build_day_picker_shortcut(), "Gun-Sec-Antrenman.shortcut"),
        (build_creatine_reminder(), "Kreatin-Hatirlatici.shortcut"),
    ]
    for workflow, name in shortcuts:
        path = write_shortcut(workflow, name)
        print(f"Created: {path} ({path.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
