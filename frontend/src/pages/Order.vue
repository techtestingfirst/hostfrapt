<script setup lang="ts">
import { reactive, computed } from 'vue'
import { Tabs } from 'frappe-ui'
import LucideBriefcase from '~icons/lucide/briefcase'
import LucideCheckCircle from '~icons/lucide/check-circle'
import LucideIndianRupee from '~icons/lucide/indian-rupee'
import LucideUser from '~icons/lucide/user'
import LucidePause from '~icons/lucide/pause'
import LucideCircleCheck from '~icons/lucide/circle-check'
import LucideAlarmClockCheck from '~icons/lucide/alarm-clock-check'
import LucideCalendar from '~icons/lucide/calendar'
import {
    Button, ListHeader, ListHeaderItem, ListRow,
    ListRowItem, ListRows, ListSelectBanner, ListView
} from 'frappe-ui'

const state = reactive({
    index: 0,
})

const tabs = computed(() =>
    [
        {
            label: 'Active',
            value: 'active',
            icon: LucideCircleCheck,
        },
        {
            label: 'Suspended',
            value: 'suspended',
            icon: LucidePause,
        },

    ],)

const custom_columns = reactive([
    { label: 'Order Number', key: 'id', icon: LucideUser },
    { label: 'Product', key: 'product', width: '200px', icon: LucideBriefcase },
    { label: 'Billing Period', key: 'billing_period', icon: LucideAlarmClockCheck },
    { label: 'Order Date', key: 'order_date', icon: LucideCalendar },
    { label: 'Amount', key: 'amount', icon: LucideIndianRupee },
    { label: 'Status', key: 'status', icon: LucideCheckCircle },
])

const custom_rows = reactive({
    active: [
        {
            id: 1,
            product: 'Shared Hosting',
            billing_period: 'Monthly',
            order_date: '2023-01-15',
            amount: 100,
            status: { label: 'Active', bg_color: 'bg-surface-green-3' },
        },
        {
            id: 3,
            product: 'Shared Hosting',
            billing_period: 'Monthly',
            order_date: '2023-01-15',
            amount: 100,
            status: { label: 'Active', bg_color: 'bg-surface-green-3' },
        },
    ],
    suspended: [
        // {
        //     id: 2,
        //     product: 'Shared Hosting',
        //     billing_period: 'Monthly',
        //     order_date: '2023-01-15',
        //     amount: 100,
        //     status: { label: 'Suspended', bg_color: 'bg-surface-red-5' },
        // },
    ]
})

</script>

<template>
    <div class="p-5 max-w-5xl mx-auto">
        <Tabs class="border rounded" v-model="state.index" :tabs="tabs">
            <template v-if="custom_rows[tab.value]" , #tab-panel="{ tab }">
                <div class="mt-4 border rounded-lg overflow-hidden bg-white">
                    <ListView class="h-[150px]" :columns="custom_columns" :rows="custom_rows[tab.value]" :options="{
                        selectable: true,
                        showTooltip: true,
                        resizeColumn: true,
                        emptyState: {
                            title: `No ${tab.value} records`,
                            description: `There are currently no items in the ${tab.value} category.`,
                            button: {
                                label: 'Add Record',
                                variant: 'solid',
                                onClick: () => console.log('Add clicked'),
                            },
                        },

                    }" row-key="id">
                        <ListHeader>
                            <ListHeaderItem v-for="column in custom_columns" :key="column.key" :item="column">
                                <template #prefix="{ item }">
                                    <component :is="item.icon" class="size-4" />
                                </template>
                            </ListHeaderItem>
                        </ListHeader>
                        <ListRows>
                            <ListRow v-for="row in custom_rows[tab.value]" :key="row.id" v-slot="{ column, item }"
                                :row="row">
                                <ListRowItem :item="item" :align="column.align">
                                    <template #prefix>
                                        <div v-if="column.key === 'status'" class="h-3 w-3 rounded-full"
                                            :class="item.bg_color" />
                                    </template>
                                </ListRowItem>
                            </ListRow>
                        </ListRows>
                        <ListSelectBanner>
                            <template #actions="{ unselectAll }">
                                <div class="flex gap-2">
                                    <Button variant="ghost" label="Delete" />
                                    <Button variant="ghost" label="Unselect all" @click="unselectAll" />
                                </div>
                            </template>
                        </ListSelectBanner>
                    </ListView>
                </div>
            </template>
            <template v-else, #tab-panel="{ tab }">
                <div class="mt-4 border rounded-lg overflow-hidden bg-white">
                    <ListView class="h-[150px]" :columns="custom_columns" :rows="custom_rows[tab.value]" :options="{
                        selectable: true,
                        showTooltip: true,
                        resizeColumn: true,
                        emptyState: {
                            title: `No ${tab.value} records`,
                            description: `There are currently no items in the ${tab.value} category.`,
                            button: {
                                label: 'Add Record',
                                variant: 'solid',
                                onClick: () => console.log('Add clicked'),
                            },
                        },

                    }" row-key="id">
                        <ListHeader>
                            <ListHeaderItem v-for="column in custom_columns" :key="column.key" :item="column">
                                <template #prefix="{ item }">
                                    <component :is="item.icon" class="size-4" />
                                </template>
                            </ListHeaderItem>
                        </ListHeader>
                    </ListView>
                </div>
            </template>
        </Tabs>
    </div>
</template>