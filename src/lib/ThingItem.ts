import { v4 as uuid } from 'uuid'

export interface ThingItemKeys {
    pk: string
    sk: string
}

export interface ThingItemData {
    [key: string]: any
}

export interface ThingItem extends ThingItemKeys, ThingItemData { }

/**
 * Create a new ThingItemKeys object with the same value for pk and sk. Key values a uuid or the 
 * optional id parameter if provided
 * @param id - optional string to use as the key value
 *
 * @returns ThingItemKeys
 */
export function createKeys(id?: string): ThingItemKeys {
    const key = id || uuid()
    return {
        pk: key,
        sk: key
    }
}

/**
 * Create a new ThingItemKeys object with the same value for pk and sk
 * @param id - string to use as the key value
 *
 * @returns ThingItemKeys
 */
export function getKeys(id: string): ThingItemKeys {
    return {
        pk: id,
        sk: id
    }
}
