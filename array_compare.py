#!/usr/bin/env python3
# array_compare.py

regex_two_groups = ['start-time-5', 'nav-item', 'ts-service-box', 'name', 'navbar-expand-lg', 'service-description', 'start-time', 'col-md-12', 'footer-logo', 'footer-social', 'pintura', 'cleaning-responsabilities', 'no-start-date', 'is-vacant-no', 'comp-email', 'bg-overlay', 'storage-no', 'label_pisos', 'demolition', 'subscribe-call-to-acton', 'exist-project-no', 'mt-3', 'project-item-title', 'navbar-dark', 'gap-60', 'no-padding', 'text-md-right', 'card', 'bg-white', 'fa-instagram', 'existing-project-yes', 'contact-form', 'slide-sub-title', 'start-after-three-months', 'd-block', 'header-one', 'top-info-box', 'action-style-box', 'fa-trophy', 'newsletter-introtext', 'navbar-collapse', 'button-look', 'ts-features', 'shuffle-btn-group', 'column-title', 'cliente-type', 'fa-thumbs-up', 'clean-duty-ownder', 'gallery-popup', 'ts-service-area', 'btn-primary', 'forro', 'card-header', 'banner-carousel-1', 'comp-whatsapp', 'text-lg-left', 'eletricos', 'ts-service-box-img', 'mt-5', 'p-0', 'ts-service-box-content', 'banner-area', 'ts-service-icon', 'info-box-subtitle-mails', 'cleaning-owner', 'hidraulicos', 'slider-description', 'have-design-no', 'materials-resp-ownder', 'emission-no', 'pisos', 'label_hidraulicos', 'site-navigation', 'collapse', 'text-md-left', 'up-to-200', 'label_up-to-200', 'navbar-toggler-icon', 'project-cat', 'label_telhado', 'fs-frm', 'logo-area', 'storage-space-yes', 'have-design-plans', 'error-container', 'service-goal', 'btn', 'show', 'shuffle-wrapper', 'nav', 'vacant-no', 'clean-duty-company', 'banner-heading', 'unit', 'immobile-type', 'logo', 'call-to-action-box', 'btn-dark', 'action-title', 'email-subject', 'text-center', 'section-title', 'more-than-200', 'into-sub-title', 'label_more-than-200', 'Nota', 'materials-resp-company', 'col-1', 'another', 'start-time-2', 'street-address', 'mb-4', 'working-hours', 'banner-carousel-item', 'img-fluid', 'up-to-150', 'col-lg-3', 'immobile-visit-no', 'top-bar', 'have-design-plans-no', 'banner-carousel', 'pb-0', 'nav-link', 'mb-3', 'form-control', 'navbar-nav', 'all', 'main-container', 'label_forro', 'existing-project', 'shuffle-sizer', 'materials-responsabilities', 'telhado', 'blank', 'label_eletricos', 'is-vacant-yes', 'start-soon', 'banner-text', 'immobile-owner-maybe', 'property-age', 'available-visit-no', 'info-box-content', 'navbar-toggler', 'into-title', 'own-immobile', 'own-immobile-maybe', 'vacant-yes', 'fab', 'col-12', 'col-lg-4', 'immobile-new', 'footer-main', 'up-to-50', 'active', 'mb-lg-0', 'col-lg-12', 'accordion', 'mr-0', 'subscribe', 'available-visit-yes', 'materials-owner', 'email-address', 'emission-yes', 'fas', 'accordion-group', 'contact-form-container', 'whatsapp-logo', 'header-right', 'slide-title', 'credit-card-yes', 'trt-emission-yes', 'dropdown-toggle', 'label_up-to-100', 'footer', 'fa-users', 'is-vacant', 'slider', 'fa', 'navbar', 'mb-0', 'gap-20', 'alvenaria', 'storage-yes', 'fs-frm-selects', 'existing-project-no', 'cleaning-company', 'start-time-1', 'own-immobile-no', 'ts-service-box-info', 'immobile-visit-yes', 'mt-md-0', 'payment-method', 'ts-service-box-bg', 'widget-title', 'banner-title', 'fa-envelope', 'col-md-5', 'row', 'container', 'storage-space', 'formaereformas', 'start-in-two-to-three-months', 'map', 'start-in-a-month', 'label_reparo', 'label_pintura', 'immobile-old', 'col-lg-9', 'have-design-yes', 'materials-company', 'align-items-center', 'slide-title-box', 'google-map', 'col-lg-6', 'section-sub-title', 'fa-sliders-h', 'fs-frm-work-type', 'fa-facebook-f', 'info-box-subtitle', 'fs-frm-inputs', 'collapsed', 'project-item-info-content', 'label_demolition', 'info-box', 'info-box-title', 'border', 'trt-emission', 'reparo', 'immobile-owner-no', 'immobile-owner-yes', 'dropdown', 'mt-lg-0', 'bg-transparent', 'solid-bg', 'new-immobile', 'body-inner', 'start-time-4', 'justify-content-between', 'ts-newsletter', 'single-project-img-container', 'col-md-6', 'label_alvenaria', 'col-md-8', 'service-box-title', 'col-lg-8', 'text-white', 'project-img-container', 'col-md-4', 'mb-md-5', 'slider-content', 'call-to-action-btn', 'mr-auto', 'card-body', 'ts-intro', 'footer-about', 'credit-card-no', 'mt-4', 'footer-widget', 'measuring', 'on-card-no', 'call-to-action-text', 'start-time-3', 'form-control-name', 'storage-space-no', 'h-100', 'btn-block', 'form-group', 'project-item-info', 'immobile-visit', 'gap-40', 'up-to-100', 'gallery-icon', 'old-immobile', 'icon-round', 'trt-emission-no', 'text-left', 'lead', 'label_up-to-150', 'label_another', 'exist-project-yes', 'on-card-yes', 'solid', 'd-flex', 'own-immobile-yes', 'class=', 'have-design-plans-yes', 'form-control-message', 'project-area', 'label_up-to-50', 'text-right']
regex_no_group = ['up-to-50', 'footer-about', 'mr-0', 'materials-owner', 'lead', 'label_more-than-200', 'fa-thumbs-up', 'mt-3', 'info-box-title', 'accordion', 'card-body', 'project-item-info', 'servicos-nav', 'storage-no', 'section-title', 'fs-frm-inputs', 'shuffle-sizer', 'immobile-owner-yes', 'start-time-5', 'existing-project-no', 'btn-dark', 'hidraulicos', 'project-nav', 'col-lg-8', 'email-address', 'action-style-box', 'working-hours', 'exist-project-no', 'have-design-plans-yes', 'start-soon', 'id=', 'blank', 'loading=', 'shuffler-section', 'text-center', 'ts-newsletter', 'all', 'fa', 'justify-content-between', 'navbar-collapse', 'ts-service-box-img', 'body-inner', 'info-box', 'gallery-icon', 'col-1', 'pisos', 'footer-main', 'label_pintura', 'border', 'text-lg-left', 'col-lg-4', 'Nota', 'service-box-title', 'col-md-5', 'storage-space', 'about', 'project-section', 'label_demolition', 'new-immobile', 'ts-service-box-bg', 'own-immobile', 'col-12', 'immobile-visit-no', 'materials-responsabilities', 'call-to-action-text', 'ts-features', 'mt-5', 'no-start-date', 'collapseOne', 'label_up-to-100', 'text-md-left', 'storage-space-no', 'trt-emission-no', 'footer-social', 'service-goal', 'action-title', 'eletricos', 'bg-white', 'ts-intro', 'own-immobile-maybe', 'col-md-6', 'call-to-action-box', 'another', 'vacant-yes', 'trt-emission-yes', 'logo-area', 'navbar-dark', 'mt-lg-0', 'fa-sliders-h', 'navbar-toggler-icon', 'up-to-100', 'comp-email', 'lazy', 'alvenaria', 'storage-yes', 'immobile-visit-yes', 'measuring', 'main-container', 'project-item-title', 'have-design-no', 'contact-form', 'cleaning-company', 'widget-title', 'mb-lg-0', 'dropdown-toggle', 'on-card-yes', 'text-white', 'slide-sub-title', 'card', 'up-to-200', 'top-info-box', 'p-0', 'banner-carousel-1', 'google-map', 'services', 'slider-content', 'collapsed', 'emission-yes', 'unit', 'is-vacant', 'own-immobile-yes', 'container', 'info-box-subtitle-mails', 'navbar', 'col-md-8', 'bg-transparent', 'newsletter-introtext', 'fs-frm-work-type', 'exist-project-yes', 'btn-primary', 'fa-trophy', 'have-design-plans-no', 'cleaning-owner', 'slide-title-box', 'contatos-nav', 'email-subject', 'info-box-subtitle', 'banner-heading', 'fas', 'navbar-toggler', 'on-card-no', 'start-time', 'footer', 'credit-card-no', 'nav-link', 'mb-0', 'immobile-new', 'materials-resp-ownder', 'button-look', 'materials-resp-company', 'comp-whatsapp', 'start-in-a-month', 'slide-title', 'forro', 'fs-frm', 'have-design-yes', 'project-cat', 'existing-project', 'collapseThree', 'd-flex', 'own-immobile-no', 'subscribe-call-to-acton', 'col-lg-12', 'label_forro', 'd-block', 'mr-auto', 'into-title', 'fa-envelope', 'contact-form-container', 'single-project-img-container', 'section-sub-title', 'inicio-nav', 'col-md-4', 'immobile-type', 'cliente-type', 'old-immobile', 'column-title', 'h-100', 'img-fluid', 'label_up-to-50', 'formaereformas', 'demolition', 'image-container', 'fab', 'storage-space-yes', 'immobile-visit', 'top-bar', 'logo', 'gap-40', 'btn', 'form-control-message', 'subscribe', 'col-lg-3', 'immobile-owner-no', 'navbar-expand-lg', 'nav', 'have-design-plans', 'more-than-200', 'accordion-group', 'banner-carousel-item', 'btn-block', 'available-visit-yes', 'text-right', 'label_hidraulicos', 'is-vacant-no', 'ts-service-box-info', 'credit-card-yes', 'col-lg-6', 'col-lg-9', 'into-sub-title', 'row', 'up-to-150', 'navbar-nav', 'mt-4', 'label_up-to-150', 'payment-method', 'start-time-3', 'service-description', 'contacts', 'name', 'ts-service-box-content', 'fa-facebook-f', 'reparo', 'label_alvenaria', 'emission-no', 'banner-text', 'form-group', 'label_up-to-200', 'banner-area', 'title-category', 'map', 'active', 'start-time-4', 'class=', 'collapseTwo', 'slider', 'call-to-action-btn', 'mb-3', 'project-item-info-content', 'immobile-owner-maybe', 'banner-carousel', 'start-time-1', 'label_telhado', 'fa-users', 'icon-round', 'label_eletricos', 'mt-md-0', 'orcamento-nav', 'col-md-12', 'mb-4', 'mb-md-5', 'whatsapp-logo', 'gallery-popup', 'footer-widget', 'solid', 'pintura', 'immobile-old', 'start-time-2', 'site-navigation', 'card-header', 'vacant-no', 'start-in-two-to-three-months', 'info-box-content', 'form-control-name', 'trt-emission', 'align-items-center', 'fs-frm-selects', 'telhado', 'text-left', 'project-img-container', 'label_another', 'available-visit-no', 'gap-20', 'start-after-three-months', 'gap-60', 'street-address', 'materials-company', 'property-age', 'slider-description', 'clean-duty-ownder', 'clean-duty-company', 'ts-service-icon', 'text-md-right', 'ts-service-box', 'label_pisos', 'label_reparo', 'existing-project-yes', 'header', 'is-vacant-yes', 'error-container', 'no-padding', 'form-control', 'fa-instagram', 'cleaning-responsabilities', 'header-right']
match = []

print(f"List of Matches Before ({len(match)})")
print(f"List of regex_two_groups Before ({len(regex_two_groups)})")
print(f"List of regex_no_group Before ({len(regex_no_group)})")

two_groups = regex_two_groups.copy()
no_groups = regex_no_group.copy()

for attr in regex_two_groups:
    # print(attr)
    # if attr is in the regex_no_group list pop and add to the list of match
        # also pop from regex_two_groups
    if attr in regex_no_group:
        match.append(attr)
        index_no_group = no_groups.index(attr)
        del no_groups[index_no_group:index_no_group+1]
        
        index_two_groups = two_groups.index(attr)
        del two_groups[index_two_groups:index_two_groups+1]

    # if it is not in the regex_no_group list, leave it in regex_two_groups list
    # print match lis
print(f"List of Matches ({len(match)}): {match}")
print("===================================================================")
# print regex_two_groups
print(f"List of regex_two_groups ({len(two_groups)}): {two_groups}")
print("===================================================================")
# # print regex_no_group
print(f"List of regex_no_group ({len(no_groups)}): {no_groups}")

# print(f"List of Matches Before ({len(match)})")
# print(f"List of regex_two_groups Before ({len(regex_two_groups)})")
# print(f"List of regex_no_group Before ({len(regex_no_group)})")