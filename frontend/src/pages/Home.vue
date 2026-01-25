<script setup lang="ts">
import { reactive } from 'vue'
import { Sidebar } from 'frappe-ui'

import Notifications from '~icons/lucide/bell'
import Services from '~icons/lucide/briefcase'
import Cart from '~icons/lucide/shopping-cart'
import Tasks from '~icons/lucide/check-square'
import Dashboard from '~icons/lucide/layout-dashboard'
import Link from '~icons/lucide/link'
import EmailTemplates from '~icons/lucide/mail'
import Moon from '~icons/lucide/moon'
import News from '~icons/lucide/newspaper'
import Settings from '~icons/lucide/settings'
import User from '~icons/lucide/user'
import Ticket from '~icons/lucide/ticket'
import Invoice from '~icons/lucide/receipt-text'

function toggleTheme() {
  const currentTheme = document.documentElement.getAttribute('data-theme')
  const newTheme = currentTheme === 'dark' ? 'light' : 'dark'
  document.documentElement.setAttribute('data-theme', newTheme)
}

const crmSidebar = reactive({
  header: {
    title: 'HostFrapt',
    subtitle: 'Jane Doe',
    logo: 'https://raw.githubusercontent.com/frappe/crm/develop/.github/logo.svg',
    menuItems: [
      { label: 'Toggle Theme', icon: Moon, onClick: toggleTheme },
      {
        label: 'Help',
        to: '/help',
        icon: Settings,
        onClick: () => alert('Help clicked!'),
      },
      {
        label: 'Logout',
        to: '/logout',
        icon: User,
        onClick: () => alert('Logging out...'),
      },
    ],
  },
  sections: [
    {
      label: '',
      items: [{ label: 'Notifications', icon: Notifications, to: '' }],
    },
    {
      label: '',
      items: [
        { label: 'Dashboard', icon: Dashboard, to: '/dashboard' },
        { label: 'Order', icon: Cart, to: '/order' },
        { label: 'Invoice', icon: Invoice, to: '/invoice' },
        { label: 'Services', icon: Services, to: '/service' },
        { label: 'Tickets', icon: Ticket, to: '/tickets' },
        { label: 'News', icon: News, to: '/news' },
        {
          label: 'Email Templates',
          icon: EmailTemplates,
          to: '/email-templates',
        },
      ],
    },
  ],
})
</script>

<template>
  <Sidebar :header="crmSidebar.header" :sections="crmSidebar.sections" />
</template>