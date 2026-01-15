<template>
  <div class="flex h-screen w-full flex-col bg-surface-white shadow">
  <Sidebar
    :sections="[
      {
        label: '',
        items: [
          {
            label: 'Notifications',
            icon: {
              name: 'lucide-bell',
              render: function render$9(_ctx, _cache) {
      return openBlock(), createElementBlock("svg", _hoisted_1$a, _cache[0] || (_cache[0] = [
        createBaseVNode(
          "path",
          { d: "M10.268 21a2 2 0 0 0 3.464 0" },
          null,
          -1
          /* HOISTED */
        ),
        createBaseVNode(
          "path",
          { d: "M3.262 15.326A1 1 0 0 0 4 17h16a1 1 0 0 0 .74-1.673C19.41 13.956 18 12.499 18 8A6 6 0 0 0 6 8c0 4.499-1.411 5.956-2.738 7.326" },
          null,
          -1
          /* HOISTED */
        )
      ]));
    },
            },
            to: '',
          },
        ],
      },
      {
        label: '',
        items: [
          {
            label: 'Leads',
            icon: {
              name: 'lucide-users',
              render: function render(_ctx, _cache) {
      return openBlock(), createElementBlock("svg", _hoisted_1$1, _cache[0] || (_cache[0] = [
        createBaseVNode(
          "path",
          { d: "M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2" },
          null,
          -1
          /* HOISTED */
        ),
        createBaseVNode(
          "path",
          { d: "M16 3.128a4 4 0 0 1 0 7.744" },
          null,
          -1
          /* HOISTED */
        ),
        createBaseVNode(
          "path",
          { d: "M22 21v-2a4 4 0 0 0-3-3.87" },
          null,
          -1
          /* HOISTED */
        ),
        createBaseVNode(
          "circle",
          {
            cx: "9",
            cy: "7",
            r: "4"
          },
          null,
          -1
          /* HOISTED */
        )
      ]));
    },
            },
            to: '/leads',
          },
          {
            label: 'Deals',
            icon: {
              name: 'lucide-briefcase',
              render: function render$8(_ctx, _cache) {
      return openBlock(), createElementBlock("svg", _hoisted_1$9, _cache[0] || (_cache[0] = [
        createBaseVNode(
          "path",
          { d: "M16 20V4a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16" },
          null,
          -1
          /* HOISTED */
        ),
        createBaseVNode(
          "rect",
          {
            width: "20",
            height: "14",
            x: "2",
            y: "6",
            rx: "2"
          },
          null,
          -1
          /* HOISTED */
        )
      ]));
    },
            },
            to: '/deals',
          },
          {
            label: 'Contacts',
            icon: {
              name: 'lucide-user-check',
              render: function render$1(_ctx, _cache) {
      return openBlock(), createElementBlock("svg", _hoisted_1$2, _cache[0] || (_cache[0] = [
        createBaseVNode(
          "path",
          { d: "m16 11 2 2 4-4" },
          null,
          -1
          /* HOISTED */
        ),
        createBaseVNode(
          "path",
          { d: "M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2" },
          null,
          -1
          /* HOISTED */
        ),
        createBaseVNode(
          "circle",
          {
            cx: "9",
            cy: "7",
            r: "4"
          },
          null,
          -1
          /* HOISTED */
        )
      ]));
    },
            },
            to: '/contacts',
          },
          {
            label: 'Organizations',
            icon: {
              name: 'lucide-building',
              render: function render$7(_ctx, _cache) {
      return openBlock(), createElementBlock("svg", _hoisted_1$8, _cache[0] || (_cache[0] = [
        createStaticVNode('<rect width="16" height="20" x="4" y="2" rx="2" ry="2"></rect><path d="M9 22v-4h6v4"></path><path d="M8 6h.01"></path><path d="M16 6h.01"></path><path d="M12 6h.01"></path><path d="M12 10h.01"></path><path d="M12 14h.01"></path><path d="M16 10h.01"></path><path d="M16 14h.01"></path><path d="M8 10h.01"></path><path d="M8 14h.01"></path>', 11)
      ]));
    },
            },
            to: '/organizations',
          },
          {
            label: 'Notes',
            icon: {
              name: 'lucide-clipboard',
              render: function render$5(_ctx, _cache) {
      return openBlock(), createElementBlock("svg", _hoisted_1$6, _cache[0] || (_cache[0] = [
        createBaseVNode(
          "rect",
          {
            width: "8",
            height: "4",
            x: "8",
            y: "2",
            rx: "1",
            ry: "1"
          },
          null,
          -1
          /* HOISTED */
        ),
        createBaseVNode(
          "path",
          { d: "M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2" },
          null,
          -1
          /* HOISTED */
        )
      ]));
    },
            },
            to: '/notes',
          },
          {
            label: 'Tasks',
            icon: {
              name: 'lucide-check-square',
              render: function render$6(_ctx, _cache) {
      return openBlock(), createElementBlock("svg", _hoisted_1$7, _cache[0] || (_cache[0] = [
        createBaseVNode(
          "path",
          { d: "M21 10.656V19a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h12.344" },
          null,
          -1
          /* HOISTED */
        ),
        createBaseVNode(
          "path",
          { d: "m9 11 3 3L22 4" },
          null,
          -1
          /* HOISTED */
        )
      ]));
    },
            },
            to: '/tasks',
          },
          {
            label: 'Call Logs',
            icon: {
              name: 'lucide-phone',
              render: function render$2(_ctx, _cache) {
      return openBlock(), createElementBlock("svg", _hoisted_1$3, _cache[0] || (_cache[0] = [
        createBaseVNode(
          "path",
          { d: "M13.832 16.568a1 1 0 0 0 1.213-.303l.355-.465A2 2 0 0 1 17 15h3a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2A18 18 0 0 1 2 4a2 2 0 0 1 2-2h3a2 2 0 0 1 2 2v3a2 2 0 0 1-.8 1.6l-.468.351a1 1 0 0 0-.292 1.233 14 14 0 0 0 6.392 6.384" },
          null,
          -1
          /* HOISTED */
        )
      ]));
    },
            },
            to: '/call-logs',
          },
          {
            label: 'Email Templates',
            icon: {
              name: 'lucide-mail',
              render: function render$4(_ctx, _cache) {
      return openBlock(), createElementBlock("svg", _hoisted_1$5, _cache[0] || (_cache[0] = [
        createBaseVNode(
          "path",
          { d: "m22 7-8.991 5.727a2 2 0 0 1-2.009 0L2 7" },
          null,
          -1
          /* HOISTED */
        ),
        createBaseVNode(
          "rect",
          {
            x: "2",
            y: "4",
            width: "20",
            height: "16",
            rx: "2"
          },
          null,
          -1
          /* HOISTED */
        )
      ]));
    },
            },
            to: '/email-templates',
          },
        ],
      },
        ],
  />
  </div>
</template>