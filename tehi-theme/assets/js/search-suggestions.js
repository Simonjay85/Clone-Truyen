(function () {
    'use strict';

    var settings = window.tehiSearchSuggestions || {};
    var forms = document.querySelectorAll('.mkm-search-form, .mkm-mobile-search');
    var minChars = Number(settings.minChars) || 2;
    var strings = settings.strings || {};

    if (!forms.length || !settings.ajaxUrl) {
        return;
    }

    function makeElement(tagName, className, text) {
        var element = document.createElement(tagName);
        if (className) {
            element.className = className;
        }
        if (typeof text === 'string') {
            element.textContent = text;
        }
        return element;
    }

    function setupForm(form, formIndex) {
        var input = form.querySelector('input[name="s"]');
        var panel = form.querySelector('.mkm-search-suggestions');
        var list = form.querySelector('.mkm-search-suggestions-list');
        var allResultsButton = form.querySelector('.mkm-search-suggestions-submit');

        if (!input || !panel || !list || !allResultsButton) {
            return null;
        }

        if (!panel.id) {
            panel.id = 'mkm-search-suggestions-' + formIndex;
        }
        input.setAttribute('role', 'combobox');
        input.setAttribute('aria-haspopup', 'listbox');
        input.setAttribute('aria-controls', panel.id);
        input.setAttribute('aria-expanded', 'false');

        var state = {
            activeIndex: -1,
            items: [],
            timer: null,
            requestId: 0,
            controller: null
        };

        function setOpen(isOpen) {
            panel.hidden = !isOpen;
            input.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
            form.classList.toggle('mkm-search-open', isOpen);
            if (!isOpen) {
                state.activeIndex = -1;
                input.removeAttribute('aria-activedescendant');
                list.querySelectorAll('.mkm-search-suggestion').forEach(function (option) {
                    option.classList.remove('is-active');
                    option.setAttribute('aria-selected', 'false');
                });
            }
        }

        function setMessage(message) {
            list.replaceChildren();
            state.items = [];
            state.activeIndex = -1;
            list.appendChild(makeElement('div', 'mkm-search-suggestions-message', message));
        }

        function updateAllResultsButton(query) {
            if (!query) {
                allResultsButton.hidden = true;
                allResultsButton.textContent = '';
                return;
            }
            allResultsButton.hidden = false;
            allResultsButton.textContent = (strings.all || 'Xem tất cả kết quả cho') + ' “' + query + '”';
        }

        function setActive(index) {
            state.activeIndex = index;
            var options = list.querySelectorAll('.mkm-search-suggestion');
            options.forEach(function (option, optionIndex) {
                var isActive = optionIndex === index;
                option.classList.toggle('is-active', isActive);
                option.setAttribute('aria-selected', isActive ? 'true' : 'false');
            });
            if (index >= 0 && options[index]) {
                input.setAttribute('aria-activedescendant', options[index].id);
                options[index].scrollIntoView({ block: 'nearest' });
            } else {
                input.removeAttribute('aria-activedescendant');
            }
        }

        function renderItems(items, query) {
            list.replaceChildren();
            state.items = Array.isArray(items) ? items : [];
            state.activeIndex = -1;

            if (!state.items.length) {
                setMessage(strings.empty || 'Chưa tìm thấy truyện phù hợp.');
            } else {
                state.items.forEach(function (item, itemIndex) {
                    var link = makeElement('a', 'mkm-search-suggestion');
                    link.href = item.url || '#';
                    link.id = panel.id + '-option-' + itemIndex;
                    link.setAttribute('role', 'option');
                    link.setAttribute('aria-selected', 'false');
                    link.setAttribute('tabindex', '-1');

                    var cover = makeElement('img', 'mkm-search-suggestion-cover');
                    cover.src = item.cover || settings.fallback || '';
                    cover.alt = '';
                    cover.loading = 'lazy';
                    cover.addEventListener('error', function () {
                        if (this.dataset.fallbackUsed || !settings.fallback) {
                            return;
                        }
                        this.dataset.fallbackUsed = '1';
                        this.src = settings.fallback;
                    });

                    var copy = makeElement('span', 'mkm-search-suggestion-copy');
                    copy.appendChild(makeElement('span', 'mkm-search-suggestion-title', item.title || 'Không có tiêu đề'));

                    var meta = makeElement('span', 'mkm-search-suggestion-meta');
                    meta.appendChild(makeElement('span', 'mkm-search-suggestion-type', item.type || 'Truyện'));
                    if (item.author) {
                        meta.appendChild(makeElement('span', 'mkm-search-suggestion-dot', '·'));
                        meta.appendChild(makeElement('span', '', item.author));
                    }
                    if (item.genre) {
                        meta.appendChild(makeElement('span', 'mkm-search-suggestion-dot', '·'));
                        meta.appendChild(makeElement('span', '', item.genre));
                    }
                    copy.appendChild(meta);

                    link.appendChild(cover);
                    link.appendChild(copy);
                    link.appendChild(makeElement('span', 'mkm-search-suggestion-arrow', '›'));

                    link.addEventListener('mouseenter', function () {
                        setActive(itemIndex);
                    });
                    link.addEventListener('focus', function () {
                        setActive(itemIndex);
                    });
                    list.appendChild(link);
                });
            }

            updateAllResultsButton(query);
            setOpen(true);
        }

        function fetchSuggestions(query) {
            var requestId = ++state.requestId;
            if (state.controller && typeof state.controller.abort === 'function') {
                state.controller.abort();
            }
            state.controller = typeof window.AbortController === 'function' ? new AbortController() : null;

            setMessage(strings.loading || 'Đang tìm gợi ý...');
            updateAllResultsButton(query);
            setOpen(true);

            var body = new URLSearchParams();
            body.set('action', 'tehi_search_suggestions');
            body.set('q', query);

            fetch(settings.ajaxUrl, {
                method: 'POST',
                credentials: 'same-origin',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
                },
                body: body.toString(),
                signal: state.controller ? state.controller.signal : undefined
            })
                .then(function (response) {
                    if (!response.ok) {
                        throw new Error('Search suggestions request failed');
                    }
                    return response.json();
                })
                .then(function (payload) {
                    if (requestId !== state.requestId) {
                        return;
                    }
                    if (!payload || !payload.success) {
                        throw new Error('Search suggestions response failed');
                    }
                    renderItems(payload.data && payload.data.items, query);
                })
                .catch(function (error) {
                    if (error && error.name === 'AbortError') {
                        return;
                    }
                    if (requestId === state.requestId) {
                        setMessage(strings.error || 'Không thể tải gợi ý lúc này.');
                        updateAllResultsButton(query);
                        setOpen(true);
                    }
                });
        }

        function scheduleFetch() {
            var query = input.value.trim();
            if (state.timer) {
                window.clearTimeout(state.timer);
            }
            if (query.length < minChars) {
                state.requestId += 1;
                if (state.controller && typeof state.controller.abort === 'function') {
                    state.controller.abort();
                }
                state.items = [];
                state.activeIndex = -1;
                updateAllResultsButton('');
                setOpen(false);
                return;
            }
            state.timer = window.setTimeout(function () {
                fetchSuggestions(query);
            }, 180);
        }

        input.addEventListener('input', scheduleFetch);
        function reopenForCurrentQuery() {
            if (input.value.trim().length >= minChars) {
                if (state.items.length) {
                    setOpen(true);
                } else {
                    scheduleFetch();
                }
            }
        }

        input.addEventListener('focus', reopenForCurrentQuery);
        input.addEventListener('click', reopenForCurrentQuery);
        input.addEventListener('keydown', function (event) {
            if (event.key === 'ArrowDown' && state.items.length) {
                event.preventDefault();
                setActive(Math.min(state.activeIndex + 1, state.items.length - 1));
            } else if (event.key === 'ArrowUp' && state.items.length) {
                event.preventDefault();
                setActive(Math.max(state.activeIndex - 1, 0));
            } else if (event.key === 'Escape' && !panel.hidden) {
                event.preventDefault();
                setOpen(false);
            } else if (event.key === 'Enter' && state.activeIndex >= 0 && state.items[state.activeIndex]) {
                event.preventDefault();
                window.location.href = state.items[state.activeIndex].url;
            }
        });

        return {
            form: form,
            close: function () {
                setOpen(false);
            }
        };
    }

    var controllers = [];
    Array.prototype.forEach.call(forms, function (form, index) {
        var controller = setupForm(form, index);
        if (controller) {
            controllers.push(controller);
        }
    });

    document.addEventListener('pointerdown', function (event) {
        controllers.forEach(function (controller) {
            if (!controller.form.contains(event.target)) {
                controller.close();
            }
        });
    });
}());
