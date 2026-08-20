# Graph Report - .  (2026-08-20)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 1280 nodes · 2446 edges · 126 communities (112 shown, 14 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS · INFERRED: 3 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `86813813`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- load_site_config
- helpers.mjs
- apply_handoff_observability_v518.py
- apply_authority_v53_core.py
- apply_experience_v60.py
- run_quality_v55.mjs
- apply_capability_truth_v521.py
- apply_experience_perspectives_v60.py
- render_catalog_static.mjs
- validate_decision_v58.py
- apply_production_v50.py
- validate_experience_v60.py
- apply_decision_action_v515.py
- demo.js
- normalize_experience_compat_v60.py
- apply_editorial_ux_v47.py
- apply_experience_sectors_v60.py
- render_services_v42.mjs
- validate_release_governance_v57.py
- apply_experience_solutions_v60.py
- main
- apply_conversion_path_v528.py
- validate_sector
- apply_engagement_clarity_v63.py
- validate_legal_intelligence_discovery_v70.py
- apply_buying_clarity_v72.py
- apply_contact_compression_v523.py
- apply_cro_v52.py
- apply_fit_scope_clarity_v64.py
- apply_handoff_v517.py
- apply_legal_intelligence_demo_v73.py
- apply_recommendation_v514.py
- enrich_editorial_pages.py
- validate_experience_perspectives_v60.py
- apply_decision_compression_v531.py
- main
- apply_legal_intelligence_discovery_v70.py
- apply_proof_v512.py
- validate_buying_clarity_v72.py
- validate_offer_narrative_v522.py
- validate_proof_v512.py
- apply_commercial_brief_v513.py
- validate_decision_action_v515.py
- validate_experience_solutions_v60.py
- validate_ai_governance_360_prototype_v70.py
- validate_experience_final_v60.py
- validate_regulatory_control_prototype_v70.py
- SiteParser
- apply_ai_governance_360_prototype_v70.py
- apply_regulatory_control_prototype_v70.py
- validate_commercial_brief_v513.py
- validate_contact_compression_v523.py
- validate_fit_scope_clarity_v64.py
- validate_live_v51.py
- validate_recommendation_v514.py
- validate_conversion_v510.py
- apply_conversion_v510.py
- apply_legal_intelligence_deep_offers_v70.py
- apply_legal_intelligence_prototype_v70.py
- apply_visual_assets.py
- validate_ci_v56.py
- validate_decision_compression_v531.py
- validate_engagement_clarity_v63.py
- validate_legal_intelligence_demo_v73.py
- apply_commercial_evidence_v74.py
- patch
- apply_operations_v49.py
- apply_ux_v45.py
- experiencia.js
- apply_quality_v48.py
- main
- validate_handoff_v517.py
- validate_legal_intelligence_deep_offers_v70.py
- validate_offer_commercial_v530.py
- validate_quality_v55.py
- MeridianoCiSummaryReporter
- apply_engagement_v511.py
- build_catalog_shells.py
- validate_browser_v54.py
- validate_commercial_evidence_v74.py
- validate_conversion_path_v528.py
- validate_editorial_ux_v47.py
- validate_funnel_trust_v529.py
- validate_handoff_observability_v518.py
- validate_legal_intelligence_prototype_v70.py
- validate_measurement_readiness_v61.py
- site-v3.js
- normalize_editorial_v47.py
- normalize_growth_compat_v51.py
- validate_decision_flow.py
- validate_detail_ux_v46.py
- validate_editorial_context.py
- validate_engagement_v511.py
- validate_legal_intelligence_v70.py
- validate_live_v49.py
- validate_page_context.py
- validate_pages_trigger_v511.py
- refresh_graphify_knowledge.sh

## God Nodes (most connected - your core abstractions)
1. `test` - 24 edges
2. `main()` - 18 edges
3. `patch_detail()` - 16 edges
4. `main()` - 16 edges
5. `load_site_config()` - 16 edges
6. `validate_sector()` - 15 edges
7. `e()` - 14 edges
8. `fail()` - 14 edges
9. `expectNoHorizontalOverflow()` - 14 edges
10. `patch()` - 13 edges

## Surprising Connections (you probably didn't know these)
- `main()` --calls--> `main()`  [EXTRACTED]
  scripts/apply_handoff_observability_v518.py → scripts/apply_capability_truth_v521.py
- `main()` --calls--> `main()`  [EXTRACTED]
  scripts/apply_handoff_observability_v518.py → scripts/apply_contact_compression_v523.py
- `main()` --calls--> `main()`  [EXTRACTED]
  scripts/apply_handoff_observability_v518.py → scripts/apply_conversion_path_v528.py
- `main()` --calls--> `main()`  [EXTRACTED]
  scripts/apply_handoff_observability_v518.py → scripts/apply_decision_compression_v531.py
- `main()` --calls--> `main()`  [EXTRACTED]
  scripts/apply_handoff_observability_v518.py → scripts/apply_experience_perspectives_v60.py

## Import Cycles
- None detected.

## Communities (126 total, 14 thin omitted)

### Community 0 - "load_site_config"
Cohesion: 0.07
Nodes (44): contact_href(), main(), managed_remove(), patch_index(), patch_sitemap(), render_hub(), render_solution(), route_cards() (+36 more)

### Community 1 - "helpers.mjs"
Cohesion: 0.07
Nodes (26): audit(), blockingImpacts, compactViolations(), publicSurfaces, releaseParts, wcagTags, DETAIL_ROUTES, SUBJECTS (+18 more)

### Community 2 - "apply_handoff_observability_v518.py"
Cohesion: 0.08
Nodes (43): demo_boundary(), e(), ensure_styles(), main(), mark_body(), patch(), patch_404(), patch_demo_surface() (+35 more)

### Community 3 - "apply_authority_v53_core.py"
Cohesion: 0.12
Nodes (35): item_list_schema(), main(), patch_home_schema(), patch_hub(), patch_perspective(), patch_sector(), patch_solution(), render_perspective_block() (+27 more)

### Community 4 - "apply_experience_v60.py"
Cohesion: 0.13
Nodes (37): body_attr(), canonical_contact_href(), contact_href_for(), detail_header(), detail_journey(), discover_detail_paths(), e(), ensure_styles() (+29 more)

### Community 5 - "run_quality_v55.mjs"
Cohesion: 0.07
Nodes (29): accessibilityAuditGaps, accessibilityDiagnostics(), aggregateMedian(), checksFor(), ciPolicyFile, compactDetail(), config, diagnostics (+21 more)

### Community 6 - "apply_capability_truth_v521.py"
Cohesion: 0.13
Nodes (24): indexable_html_targets(), is_noindex(), main(), normalize_public_demo_links(), patch_demo_contract(), patch_demo_runtime(), patch_runtime_config(), patch_status() (+16 more)

### Community 7 - "apply_experience_perspectives_v60.py"
Cohesion: 0.17
Nodes (25): article_hero_parts(), authority_block(), central_decision(), clean(), e(), ensure_styles(), extract_hub_legacy(), extract_main() (+17 more)

### Community 8 - "render_catalog_static.mjs"
Cohesion: 0.16
Nodes (22): bodyInner(), bodyInnerProduct(), bodyInnerService(), cards(), catalogFiles, contactBlock(), end, enhanceHeadAndScripts() (+14 more)

### Community 9 - "validate_decision_v58.py"
Cohesion: 0.17
Nodes (17): detail_composition(), fail(), first_title(), load_catalog(), main(), Path, Devuelve la composición que debe conservar la relación v5.8 → #detail-page., route_keys() (+9 more)

### Community 10 - "apply_production_v50.py"
Cohesion: 0.18
Nodes (20): html_targets(), main(), manage_cname(), managed_remove(), normalize_referrer_meta(), patch_html(), patch_page_context(), patch_privacy() (+12 more)

### Community 11 - "validate_experience_v60.py"
Cohesion: 0.28
Nodes (21): anchor_href(), assert_contains(), assert_once(), body_attr(), count_public_html(), fail(), first_layer(), legacy_block() (+13 more)

### Community 12 - "apply_decision_action_v515.py"
Cohesion: 0.20
Nodes (20): compact_recommendation_v520(), compress_home_v520(), current_version_at_least(), ensure_head_item(), home_decision_v520(), load_contract(), main(), modality_from_detail() (+12 more)

### Community 13 - "demo.js"
Cohesion: 0.12
Nodes (15): enterPortal(), escapeHtml(), loginForm, loginView, openPanel(), portalView, renderTickets(), savedUser (+7 more)

### Community 14 - "normalize_experience_compat_v60.py"
Cohesion: 0.23
Nodes (19): main(), normalize_ai_governance_360_prototype(), normalize_buying_clarity_v72(), normalize_commercial_evidence_v74(), normalize_engagement_clarity(), normalize_home_contact_contract(), normalize_home_trust(), normalize_legal_intelligence_demo_v73() (+11 more)

### Community 15 - "apply_editorial_ux_v47.py"
Cohesion: 0.32
Nodes (18): add_assets(), add_menu(), add_mobile_cta(), contact_href(), ensure_body_metadata(), main(), page_context(), patch() (+10 more)

### Community 16 - "apply_experience_sectors_v60.py"
Cohesion: 0.23
Nodes (18): all_tags(), articles(), body_attr(), clean(), e(), ensure_styles(), extract_legacy(), extract_main() (+10 more)

### Community 17 - "render_services_v42.mjs"
Cohesion: 0.21
Nodes (15): bodyInner(), cards(), contactBlock(), enhanceHeadAndScripts(), entries, escapeHtml(), heroInner(), limitsBlock() (+7 more)

### Community 18 - "validate_release_governance_v57.py"
Cohesion: 0.21
Nodes (14): datetime, count(), main(), main(), parse_ts(), seconds(), fail(), load_json() (+6 more)

### Community 19 - "apply_experience_solutions_v60.py"
Cohesion: 0.28
Nodes (16): contact_href(), e(), ensure_styles(), extract_legacy(), extract_main(), load(), main(), mark_body() (+8 more)

### Community 20 - "main"
Cohesion: 0.24
Nodes (15): ensure_css(), esc(), firm_block(), home_block(), main(), Retira solo el bloque propio y, como máximo, su salto de línea final., strip_block(), update_person_schema() (+7 more)

### Community 21 - "apply_conversion_path_v528.py"
Cohesion: 0.25
Nodes (15): depth_markup(), extract_contact_section(), main(), normalize_contact_block(), normalize_css_link(), normalize_focusable_decks(), normalize_layout_whitespace(), patch_home() (+7 more)

### Community 22 - "validate_sector"
Cohesion: 0.33
Nodes (15): article_truth(), assert_contains(), assert_once(), clean(), fail(), first_layer(), legacy_block(), main() (+7 more)

### Community 23 - "apply_engagement_clarity_v63.py"
Cohesion: 0.28
Nodes (14): body_attr(), discover_pages(), e(), ensure_nav(), ensure_section(), ensure_stylesheet(), load_json(), load_sources() (+6 more)

### Community 24 - "validate_legal_intelligence_discovery_v70.py"
Cohesion: 0.41
Nodes (14): architecture_labels(), esc(), fail(), main(), Path, require_values(), surface_block(), validate_common() (+6 more)

### Community 25 - "apply_buying_clarity_v72.py"
Cohesion: 0.31
Nodes (13): body_attr(), e(), ensure_style(), load_json(), load_paths(), load_sources(), main(), materialize() (+5 more)

### Community 26 - "apply_contact_compression_v523.py"
Cohesion: 0.26
Nodes (13): block(), main(), managed_pattern(), normalize_form_marker(), patch_home(), process_markup(), Pattern, qualification_without_summary() (+5 more)

### Community 27 - "apply_cro_v52.py"
Cohesion: 0.31
Nodes (13): css_block(), faq_schema(), main(), patch_hub(), patch_solution(), render_faq(), render_fit(), render_objections() (+5 more)

### Community 28 - "apply_fit_scope_clarity_v64.py"
Cohesion: 0.31
Nodes (13): body_attr(), discover_pages(), e(), ensure_section(), ensure_stylesheet(), load_json(), load_sources(), main() (+5 more)

### Community 29 - "apply_handoff_v517.py"
Cohesion: 0.25
Nodes (13): contact_pages(), ensure_head_item(), ensure_script(), main(), panel_markup(), patch_home(), patch_site_runtime(), public_html() (+5 more)

### Community 30 - "apply_legal_intelligence_demo_v73.py"
Cohesion: 0.30
Nodes (13): e(), ensure_style(), expected_content(), load_json(), main(), metric_rows(), Path, render_card() (+5 more)

### Community 31 - "apply_recommendation_v514.py"
Cohesion: 0.27
Nodes (13): direct_href(), ensure_head_item(), existing_direct_context(), form_block(), home_block(), load_contract(), main(), modality_from_detail() (+5 more)

### Community 32 - "enrich_editorial_pages.py"
Cohesion: 0.31
Nodes (13): absolute_url(), breadcrumb_schema(), contact_url(), enrich(), head_block(), main(), managed_pattern(), prefix_for() (+5 more)

### Community 33 - "validate_experience_perspectives_v60.py"
Cohesion: 0.38
Nodes (13): assert_contains(), assert_once(), balanced_tag_block(), clean(), fail(), hub_cards(), hub_legacy(), main() (+5 more)

### Community 34 - "apply_decision_compression_v531.py"
Cohesion: 0.33
Nodes (12): ensure_style(), main(), patch_detail(), patch_solution(), Path, semver(), solution_close(), solution_open() (+4 more)

### Community 35 - "main"
Cohesion: 0.29
Nodes (11): ensure_css(), main(), remove_managed(), remove_redundant_band(), semver(), signal_block(), validate_assets(), main() (+3 more)

### Community 36 - "apply_legal_intelligence_discovery_v70.py"
Cohesion: 0.33
Nodes (12): esc(), expected(), main(), Path, Backward-compatible renderer for the first v7.1 prototype contract., render_home(), render_hub(), render_installed() (+4 more)

### Community 37 - "apply_proof_v512.py"
Cohesion: 0.31
Nodes (12): detail_block(), ensure_style(), home_block(), load_catalog(), main(), pair_list(), pairs(), patch_detail() (+4 more)

### Community 38 - "validate_buying_clarity_v72.py"
Cohesion: 0.44
Nodes (12): body_attr(), contains(), fail(), load_json(), load_paths(), load_sources(), main(), Path (+4 more)

### Community 39 - "validate_offer_narrative_v522.py"
Cohesion: 0.42
Nodes (12): fail(), load_contract(), main(), page_map(), Path, safe_meridiano_reference(), static_body(), validate_catalog_capability_truth() (+4 more)

### Community 40 - "validate_proof_v512.py"
Cohesion: 0.35
Nodes (12): balanced_tag_block(), detail_composition(), load_catalog(), main(), Path, Aísla el elemento balanceado que contiene marker, tolerando tags anidados., require(), route_keys() (+4 more)

### Community 41 - "apply_commercial_brief_v513.py"
Cohesion: 0.33
Nodes (11): add_query_params(), brief_block(), direct_whatsapp_href(), ensure_head_item(), main(), modality_for(), patch_detail(), patch_home() (+3 more)

### Community 42 - "validate_decision_action_v515.py"
Cohesion: 0.42
Nodes (11): contract(), href_params(), main(), modality(), require(), validate_details(), validate_e2e(), validate_home() (+3 more)

### Community 43 - "validate_experience_solutions_v60.py"
Cohesion: 0.50
Nodes (11): assert_contains(), assert_once(), fail(), first_layer(), legacy(), load(), main(), Path (+3 more)

### Community 44 - "validate_ai_governance_360_prototype_v70.py"
Cohesion: 0.47
Nodes (10): deep_markers(), escaped(), fail(), main(), Path, validate_capability_boundaries(), validate_deep(), validate_links() (+2 more)

### Community 45 - "validate_experience_final_v60.py"
Cohesion: 0.53
Nodes (10): assert_once(), fail(), main(), read(), validate_404(), validate_common(), validate_demo(), validate_experience() (+2 more)

### Community 46 - "validate_regulatory_control_prototype_v70.py"
Cohesion: 0.45
Nodes (10): deep_markers(), escaped(), fail(), main(), Path, validate_boundaries(), validate_deep(), validate_links() (+2 more)

### Community 47 - "SiteParser"
Cohesion: 0.25
Nodes (6): local_target(), main(), HTMLParser, SiteParser, validate(), version_tuple()

### Community 48 - "apply_ai_governance_360_prototype_v70.py"
Cohesion: 0.44
Nodes (9): deep_markers(), esc(), expected_deep(), expected_route(), main(), Path, render_deep(), render_route() (+1 more)

### Community 49 - "apply_regulatory_control_prototype_v70.py"
Cohesion: 0.44
Nodes (9): deep_markers(), esc(), expected_deep(), expected_route(), main(), Path, render_deep(), render_route() (+1 more)

### Community 50 - "validate_commercial_brief_v513.py"
Cohesion: 0.44
Nodes (9): href_params(), main(), modality_for(), Path, require(), validate_detail(), validate_home(), validate_site_js() (+1 more)

### Community 51 - "validate_contact_compression_v523.py"
Cohesion: 0.53
Nodes (9): bounded(), main(), require(), semver(), validate_chain(), validate_e2e(), validate_home(), validate_runtime() (+1 more)

### Community 52 - "validate_fit_scope_clarity_v64.py"
Cohesion: 0.44
Nodes (9): body_attr(), extract_rows(), load_json(), main(), normalize(), pages(), Path, sources() (+1 more)

### Community 53 - "validate_live_v51.py"
Cohesion: 0.42
Nodes (6): get(), main(), main(), semver(), main(), main()

### Community 54 - "validate_recommendation_v514.py"
Cohesion: 0.51
Nodes (9): load_contract(), main(), require(), validate_details(), validate_e2e(), validate_home(), validate_js(), validate_workflows() (+1 more)

### Community 55 - "validate_conversion_v510.py"
Cohesion: 0.53
Nodes (8): fail(), main(), Path, validate_contract(), validate_detail(), validate_e2e(), validate_home(), validate_runtime()

### Community 56 - "apply_conversion_v510.py"
Cohesion: 0.43
Nodes (7): close_block(), main(), patch_detail(), patch_index(), Path, remove_block(), semver()

### Community 57 - "apply_legal_intelligence_deep_offers_v70.py"
Cohesion: 0.46
Nodes (7): esc(), expected_content(), main(), markers(), Path, render(), strip_existing()

### Community 58 - "apply_legal_intelligence_prototype_v70.py"
Cohesion: 0.43
Nodes (7): esc(), main(), materialized_content(), Path, render(), run_deep_offer_materializer(), strip_existing()

### Community 59 - "apply_visual_assets.py"
Cohesion: 0.36
Nodes (7): patch(), Path, Restaura solo durante composición las anclas que v4.5 todavía necesita.      v5., Elimina una copia previa sin alterar el resto de la línea o del documento., rehydrate_v526_ux_anchors(), remove_managed_tag(), version_tuple()

### Community 60 - "validate_ci_v56.py"
Cohesion: 0.46
Nodes (7): action_count(), action_ref(), main(), Return the stronger v5.7 SHA ref when policy exists, otherwise historical @vN., require(), section(), semver()

### Community 61 - "validate_decision_compression_v531.py"
Cohesion: 0.61
Nodes (7): details_opening(), fail(), main(), semver(), validate_contract(), validate_deep(), validate_solutions()

### Community 62 - "validate_engagement_clarity_v63.py"
Cohesion: 0.46
Nodes (7): body_attr(), e(), extract_group(), load_json(), load_sources(), main(), Path

### Community 63 - "validate_legal_intelligence_demo_v73.py"
Cohesion: 0.57
Nodes (7): fail(), link_exists(), load_json(), main(), Path, source_for(), validate_lifecycle()

### Community 64 - "apply_commercial_evidence_v74.py"
Cohesion: 0.52
Nodes (6): load_contract(), main(), materialize(), render_block(), resolve_lifecycle(), script_src()

### Community 65 - "patch"
Cohesion: 0.48
Nodes (6): main(), patch(), Path, remove_managed_block(), remove_managed_line(), replace_one()

### Community 66 - "apply_operations_v49.py"
Cohesion: 0.52
Nodes (6): ensure_maxlength_v523(), main(), patch_index(), patch_site_js(), Desde v5.23 conserva el campo por name y normaliza maxlength sin depender del or, semver()

### Community 67 - "apply_ux_v45.py"
Cohesion: 0.52
Nodes (6): main(), normalize_contact_synthesis_v523(), Convierte el wrapper v5.23 materializado antiguo antes de la extracción v4.5., replace_tag_block(), section(), version_at_least()

### Community 68 - "experiencia.js"
Cohesion: 0.47
Nodes (3): createResult(), evidenceNote(), urgencyNote()

### Community 69 - "apply_quality_v48.py"
Cohesion: 0.60
Nodes (5): main(), patch_index(), patch_js(), patch_misc(), seo()

### Community 70 - "main"
Cohesion: 0.60
Nodes (4): fail(), main(), main(), semver()

### Community 71 - "validate_handoff_v517.py"
Cohesion: 0.60
Nodes (5): contact_pages(), main(), public_html(), Path, require()

### Community 72 - "validate_legal_intelligence_deep_offers_v70.py"
Cohesion: 0.67
Nodes (5): fail(), main(), markers(), validate_source_support(), visible()

### Community 73 - "validate_offer_commercial_v530.py"
Cohesion: 0.60
Nodes (5): main(), semver(), source_ids(), validate_contract(), validate_pages()

### Community 74 - "validate_quality_v55.py"
Cohesion: 0.53
Nodes (5): action_major_present(), main(), Accept the historical major tag or a stronger SHA pin declared by v5.7 policy., require(), semver()

### Community 77 - "apply_engagement_v511.py"
Cohesion: 0.83
Nodes (3): block(), main(), remove_block()

### Community 78 - "build_catalog_shells.py"
Cohesion: 0.83
Nodes (3): json_ld(), main(), render()

### Community 79 - "validate_browser_v54.py"
Cohesion: 0.83
Nodes (3): main(), require(), semver()

### Community 80 - "validate_commercial_evidence_v74.py"
Cohesion: 1.00
Nodes (3): fail(), main(), resolve_lifecycle()

### Community 81 - "validate_conversion_path_v528.py"
Cohesion: 0.83
Nodes (3): main(), require(), semver()

### Community 82 - "validate_editorial_ux_v47.py"
Cohesion: 0.83
Nodes (3): between(), fail(), semver_tuple()

### Community 83 - "validate_funnel_trust_v529.py"
Cohesion: 0.83
Nodes (3): main(), require(), semver()

### Community 84 - "validate_handoff_observability_v518.py"
Cohesion: 0.83
Nodes (3): main(), require(), semver()

### Community 85 - "validate_legal_intelligence_prototype_v70.py"
Cohesion: 1.00
Nodes (3): fail(), main(), validate_deep_offers()

## Knowledge Gaps
- **62 isolated node(s):** `users`, `titles`, `statusLabels`, `loginView`, `portalView` (+57 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **14 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `main()` connect `apply_capability_truth_v521.py` to `apply_handoff_observability_v518.py`?**
  _High betweenness centrality (0.048) - this node is a cross-community bridge._
- **Why does `main()` connect `apply_handoff_observability_v518.py` to `apply_decision_compression_v531.py`, `main`, `apply_experience_v60.py`, `apply_capability_truth_v521.py`, `apply_experience_perspectives_v60.py`, `normalize_experience_compat_v60.py`, `apply_experience_sectors_v60.py`, `apply_experience_solutions_v60.py`, `main`, `apply_conversion_path_v528.py`, `apply_contact_compression_v523.py`?**
  _High betweenness centrality (0.046) - this node is a cross-community bridge._
- **Why does `load_site_config()` connect `load_site_config` to `apply_production_v50.py`, `apply_authority_v53_core.py`, `apply_capability_truth_v521.py`?**
  _High betweenness centrality (0.025) - this node is a cross-community bridge._
- **What connects `users`, `titles`, `statusLabels` to the rest of the system?**
  _62 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `load_site_config` be split into smaller, more focused modules?**
  _Cohesion score 0.06830601092896176 - nodes in this community are weakly interconnected._
- **Should `helpers.mjs` be split into smaller, more focused modules?**
  _Cohesion score 0.07268170426065163 - nodes in this community are weakly interconnected._
- **Should `apply_handoff_observability_v518.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07591836734693877 - nodes in this community are weakly interconnected._