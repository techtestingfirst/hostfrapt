<script setup lang="ts">
import { reactive, computed, h } from 'vue'
import {
  Tabs,
  ListView,
  Avatar,
  Badge,
  ListHeader,
  ListHeaderItem,
  ListRows,
  ListRow,
  ListRowItem,
  ListSelectBanner,
  Button
} from 'frappe-ui'

// Icons
import LucideAtSign from '~icons/lucide/at-sign'
import LucideCheckCircle from '~icons/lucide/check-circle'
import LucideUsers from '~icons/lucide/users'
import LucideUser from '~icons/lucide/user'

const state = reactive({
  tabIndex: 0,
})

// Columns Definition
const columns = [
  { label: 'Name', key: 'name', width: 3, icon: LucideUser },
  { label: 'Email', key: 'email', width: '200px', icon: LucideAtSign },
  { label: 'Role', key: 'role', icon: LucideUsers },
  { label: 'Status', key: 'status', icon: LucideCheckCircle },
]

// Data for Paid/Unpaid
const data = reactive({
  paid: [
    {
      id: 1,
      name: { label: 'John Doe' },
      email: 'john@doe.com',
      status: { label: 'Paid', bg_color: 'bg-green-500' },
      role: { label: 'Developer', color: 'green' },
    }
  ],
  unpaid: [] // Empty to demonstrate empty state
})

const tabs = computed(() => [
  { label: 'Paid', value: 'paid', count: data.paid.length },
  { label: 'Unpaid', value: 'unpaid', count: data.unpaid.length },
])
</script>

<template>
  <div class="p-5 max-w-5xl mx-auto">
    <Tabs v-model="state.tabIndex" :tabs="tabs" class="mb-4">
      <template #tab-panel="{ tab }">
        <div class="mt-4 border rounded-lg overflow-hidden bg-white">
          <ListView class="h-[400px]" :columns="columns" :rows="data[tab.value]" :options="{
            selectable: true,
            showTooltip: true,
            resizeColumn: true,
            emptyState: {
              title: `No ${tab.label} records`,
              description: `There are currently no items in the ${tab.label} category.`,
              button: {
                label: 'Add Record',
                variant: 'solid',
                onClick: () => console.log('Add clicked'),
              },
            },
          }" row-key="id">
            <ListHeader>
              <ListHeaderItem v-for="column in columns" :key="column.key" :item="column">
                <template #prefix="{ item }">
                  <component :is="item.icon" class="size-4" />
                </template>
              </ListHeaderItem>
            </ListHeader>

            <ListRows>
              <ListRow v-for="row in data[tab.value]" :key="row.id" v-slot="{ column, item }" :row="row">
                <ListRowItem :item="item">
                  <template #prefix>
                    <div v-if="column.key === 'status'" class="h-2 w-2 rounded-full mr-2" :class="item.bg_color" />
                    <Avatar v-if="column.key === 'name'" shape="circle" :image="item.image" size="sm" class="mr-2" />
                  </template>

                  <Badge v-if="column.key === 'role'" variant="subtle" :theme="item.color" size="md"
                    :label="item.label" />
                </ListRowItem>
              </ListRow>
            </ListRows>

            <ListSelectBanner>
              <template #actions="{ unselectAll }">
                <div class="flex gap-2">
                  <Button variant="ghost" label="Delete" intent="danger" />
                  <Button variant="ghost" label="Unselect all" @click="unselectAll" />
                </div>
              </template>
            </ListSelectBanner>
          </ListView>

        </div>
      </template>
    </Tabs>
  </div>
</template>